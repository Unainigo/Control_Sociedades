from sqlalchemy import Column, String, DateTime, Integer
from datetime import datetime
from database import Base

class Actividades(Base):
    __tablename__ = "actividades"
    id_actividad = Column(Integer, primary_key=True, autoincrement=True)
    create_at = Column(DateTime, default=datetime.now)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)