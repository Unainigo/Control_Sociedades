from sqlalchemy import Column, String, DateTime, Integer
from datetime import datetime
from database import Base

class Reservas(Base):
    __tablename__ = "reservas"
    id_reserva = Column(Integer, primary_key=True, autoincrement=True)
    create_at = Column(DateTime, default=datetime.now)
    id_mesa = Column(Integer, nullable=False)
    id_user = Column(Integer, nullable=False)
    id_actividad = Column(Integer, nullable=True)
    reservation_time = Column(DateTime, nullable=False)
    participants = Column(Integer, nullable=False)