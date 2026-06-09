from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from datetime import datetime
from database import Base

class Compra(Base):
    __tablename__ = "compras"
    id_compra = Column(Integer, primary_key=True, autoincrement=True)
    create_at = Column(DateTime, default=datetime.now)
    id_producto = Column(Integer, ForeignKey("productos.id_producto"), nullable=False)
    id_user = Column(Integer, ForeignKey("users.id_user"), nullable=False)
    quantity = Column(Integer, nullable=False)