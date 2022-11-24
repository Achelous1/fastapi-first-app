from fastapi import FastAPI
from typing import List
from starlette.middleware.cors import CORSMiddleware

from .db import session
from .model import User, UserTable

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/users")
def get_user_list():
    user_list = session.query(UserTable).all()
    return {"userList" : user_list}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = session.query(UserTable).filter(UserTable.id == user_id).first()
    return user


@app.post("/users")
def create_user(name: str, age: int):

    user = UserTable()
    user.name = name
    user.age = age

    session.add(user)
    session.commit()

    return f"{name} created"


@app.put("/users/")
def update_user(users: List[User]):

    for i in users:
        user = session.query(UserTable).filter(UserTable.id == i.id).first()
        user.name = i.name
        user.age = i.age
        session.commit()
        
    return user


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    user = session.query(UserTable).filter(UserTable.id == user_id).delete()
    session.commit()
    return "User is deleted"
