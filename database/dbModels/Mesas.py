from sqlalchemy import Column, String, DateTime, Integer
from datetime import datetime
from database import Base
class Mesas(Base):
    __tablename__ = "mesas"
    id_mesa = Column(Integer, primary_key=True, autoincrement=True)
    create_at = Column(DateTime, default=datetime.now)
    name = Column(String(255), unique=True, nullable=False)
    capacity = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)