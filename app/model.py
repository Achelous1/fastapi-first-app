from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, Field
from .db import Base, ENGINE


class UserTable(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)


class User(BaseModel):
    id: int
    user_name: str = Field(alias="userName")
    age: int