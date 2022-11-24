from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


user_name = "guest"
password = "guestpassword"
db_host = "localhost"
db_name = "fast_app"

DATABASE = 'mysql+pymysql://%s:%s@%s/%s?charset=utf8mb4' % (
    user_name, 
    password, 
    db_host, 
    db_name
)

ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()
