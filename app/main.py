from fastapi import FastAPI, Depends
from typing import List
from fastapi.middleware.cors import CORSMiddleware

from .db import session
from .model import User, UserTable
from .dependencies import get_query_token, get_token_header
from .routers import users

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users.router)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def index():
    return {"message": "Ok"}