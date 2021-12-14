from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import schemas, models, oauth2
from .. database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from sqlalchemy import func


router = APIRouter(
    prefix='/posts',
    tags=['Posts']
)

@router.get('/', response_model = List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).all()
    return posts

@router.get('/{id}', response_model = schemas.PostOut)
def get_id(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'post of id {id} was not found')
    return post

@router.post('/', status_code = status.HTTP_201_CREATED,response_model = schemas.Post)
def create(request: schemas.PostCreate,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    new_post = models.Post(owner_id=current_user.id, **request.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED, response_model=schemas.PostBase)
def update(id: int, request: schemas.PostBase,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'post of id {id} was not found')
    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Not authorised to perform this action',
        )

    post_query.update(request.dict())
    db.commit()
    return request

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'post with id {id} does not exist')

    if post.owner_id != current_user.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN,detail=f'Not authorised to perform this action')
    post_query.delete(synchronize_session=False)
    db.commit()
    return post

