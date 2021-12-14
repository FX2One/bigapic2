from app import schemas
from .database import session, client
import pytest
from jose import jwt
from app.config import settings


def test_create_user(client):
    res = client.post("/users/", json={'email': 'hello@email.com','password': 'pass123'})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello@email.com"
    assert res.status_code == 201

def test_login_user(client, test_user):
    res = client.post("/login", data={'username': test_user['email'],'password': test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, settings.algorithm)
    id: str = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == 'bearer'
    assert res.status_code == 200

@pytest.mark.parametrize('email, password, status_code', [
    ('mail@mail.com','pass321',403),
    ('mail2@mail.com','pass333',403),
    ('hello@email.com','pass123',422),
    ('mail5@mail.com','pass332121',403),
    ('mail6@mail.com','pass322131',403),
    ('hello@email.com','pass123',403),
])
def test_incorrect_login(client, test_user, email, password, status_code):
    res = client.post("/login", data={'username': email,'password': password})
    assert res.status_code == 403
    assert res.json().get('detail') == "Invalid Credentials"

