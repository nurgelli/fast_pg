from sqlalchemy.orm import declarative_base
from sqlalchemy import (Column, String, Integer)


Base  = declarative_base()

class Category(Base):
    __tablename__ = "category"
    
    id = Column(Integer, primary_key=True)