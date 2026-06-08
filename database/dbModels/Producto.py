from sqlalchemy import Column, String, DateTime, Integer
from datetime import datetime
from database import Base

class Producto(Base):
    __tablename__ = "productos"
    id_producto = Column(Integer, primary_key=True, autoincrement=True)
    create_at = Column(DateTime, default=datetime.now)
    name = Column(String(255), unique=True, nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)