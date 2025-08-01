import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DEV_DATABASE_URL = os.getenv("DEV_DATABASE_URL")

engine = create_engine(DEV_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush=True, bind=True)


def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()