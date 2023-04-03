from config.db import Base, meta
from sqlalchemy import Column, DateTime, Float, Integer, String, Table
from sqlalchemy.sql import func


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    img_url = Column(String)
    created_at=Column(DateTime(timezone=True), default=func.now())
    updated_at=Column(DateTime(timezone=True), onupdate=func.now())

