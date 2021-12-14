from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import schemas, models, utils
from .. database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.get('/', response_model = List[schemas.UserOut])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@router.get('/{id}', response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'user of {id} does not exist')
    return user

@router.post('/', status_code = status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hashed(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'post with id {id} does not exist')
    user.delete(synchronize_session=False)
    db.commit()
    return user