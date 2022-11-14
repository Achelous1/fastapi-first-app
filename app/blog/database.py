from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLITE_DATABASE_URL = 'sqlite:///../blog.db'

engine = create_engine(SQLITE_DATABASE_URL, connection_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()