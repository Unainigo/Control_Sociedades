from sqlalchemy import Column, String, DateTime, Integer
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"
    id_user = Column(Integer, primary_key=True, autoincrement=True)
    create_at = Column(DateTime, default=datetime.now)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), unique=True, nullable=False)