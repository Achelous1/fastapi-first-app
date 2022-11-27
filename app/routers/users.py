from fastapi import APIRouter, Depends, HTTPException
from typing import List

from ..dependencies import get_token_header
from ..model import User, UserTable
from ..db import session

router = APIRouter(
    prefix="/users",
    tags=["사용자"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}}
)


@router.get("")
def get_user_list():
    user_list = session.query(UserTable).all()
    return {"userList" : user_list}


@router.get("/{user_id}")
def get_user(user_id: int):
    user = session.query(UserTable).filter(UserTable.id == user_id).first()
    return user


@router.post("/")
def create_user(user: User):

    user = UserTable()
    user.user_name = user_name
    user.age = age

    session.add(user)
    session.commit()

    return f"{name} created"


@router.put("/")
def update_user(users: List[User]):

    for i in users:
        user = session.query(UserTable).filter(UserTable.id == i.id).first()
        user.user_name = i.user_name
        user.age = i.age
        session.commit()
        
    return user


@router.delete("/{user_id}")
def delete_user(user_id: int):
    user = session.query(UserTable).filter(UserTable.id == user_id).delete()
    session.commit()
    return user
