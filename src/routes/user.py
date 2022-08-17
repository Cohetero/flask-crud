from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT
from settings.common import Session
from models.users import User
from schemas.user import Users
from typing import List

session = Session()
user = APIRouter()

@user.get('/users/', response_model=List[Users], tags=["users"])
def get_users():
    return session.query(User.id,
                        User.name,
                        User.email,
                        User.foto).all()

@user.get('/users/{id}/', response_model=Users, tags=["users"])
def get_user(id: int):
    return session.query(User.id,
                        User.name,
                        User.email,
                        User.foto).filter(User.id == id).first()

@user.post('/users/', response_model=Users, tags=["users"])
def create_user(user: Users):
    user = User(name = user.name, email = user.email)
    session.add(user)
    session.commit()
    return "create user"

@user.put('/users/{id}/', response_model=Users, tags=["users"])
def update_user(id: int, user: Users):
    session.query(User).filter(
        User.id == id
    ).update(
        {
            User.name: user.name,
            User.email: user.email,
        }
    )
    session.commit()
    return "update user"

@user.delete('/users/{id}/', status_code=HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(id: str):
    session.query(User).filter(
        User.id == id
    ).delete()
    session.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)