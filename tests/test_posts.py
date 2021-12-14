from typing import List
from app import schemas
import pytest

def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get('/posts/')
    def validate(post):
        return schemas.PostOut(**post)

    posts_map = map(validate, res.json())
    posts_list = list(posts_map)
    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200
    #assert posts_list[0].Post.id == test_posts[0].id

'''def test_unauthroized_user_get_all_posts(client, test_posts):
    res = client.get('/posts/')
    assert res.status_code == 401

def test_unauthroized_user_get_one_post(client, test_posts):
    res = client.get(f'/posts/{test_posts[0].id}')
    assert res.status_code == 401

def test_get_one_post_not_exist(authorized_client, test_posts):
    res = authorized_client.get('/posts/88888')
    assert res.status_code == 404

def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f'/posts/{test_posts[0].id}')
    assert res.status_code == 200
    post = schemas.PostOut(**res.json())
    assert post.Post.id == test_posts[0].id
    assert post.Post.content == '1st content'

@pytest.mark.parametrize("title, content, published", [
    ('awesome title','1st content of awesome', True),
    ('awesome title2','2 contwadaw', True),
    ('aweswadawome titl21e','1st c of awesome', False),
    ('awewuhuuu','1stobobobobobo of awesome', False),
])
def test_create_post(authorized_client, test_user ,test_posts, title, content, published):
    res = authorized_client.post('/posts/',json={'title':title, 'content':content, 'published':published})
    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published
    assert created_post.owner_id == test_user['id']


def test_delete_post_unauthorized(client, test_user, test_posts):
    res = client.delete(f'/posts/{test_posts[0].id}')
    assert res.status_code == 401

def test_delete_post_success(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f'/posts/{test_posts[0].id}')
    assert res.status_code == 204

def test_delete_post_non_exist(authorized_client,test_user, test_posts):
    res = authorized_client.delete('/posts/999999')
    assert res.status_code == 404

def test_delete_other_user_post(authorized_client,test_user,test_posts):
    res = authorized_client.delete(f'/posts/{test_posts[2].id}')
    assert res.status_code == 403'''

'''def test_update_post(authorized_client, test_user, test_posts):
    data = {
        'title':'updated title',
        'content':'updated content',
        'id': test_posts[0].id
    }
    res = authorized_client.put(f'/posts/{test_posts[0].id}', json=data)
    updated_post = schemas.PostBase(**res.json())
    print(updated_post)
    assert res.status_code == 202
    assert updated_post.title == data['title']
    assert updated_post.content == data['content']

def test_update_other_user_post(authorized_client,test_user, test_user2, test_posts):
    data = {
        'title':'updated title2',
        'content':'updated content2',
        'id': test_posts[2].id
    }
    res = authorized_client.put(f'/posts/{test_posts[2].id}', json=data)
    assert res.status_code == 403

def test_update_by_unauthorized_user(client, test_user, test_posts):
    data = {
        'title':'updated title',
        'content':'updated content',
        'id': test_posts[0].id
    }
    res = client.put(f'/posts/{test_posts[0].id}', json=data)
    assert res.status_code == 401

def test_update_non_existent_post(authorized_client,test_user, test_posts):
    data = {
        'title':'updated title',
        'content':'updated content',
        'id': test_posts[0].id
    }
    res = authorized_client.put('/posts/999999', json=data)
    assert res.status_code == 404
'''

