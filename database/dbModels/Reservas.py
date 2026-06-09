from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from datetime import datetime
from database import Base

class Reservas(Base):
    __tablename__ = "reservas"
    id_reserva = Column(Integer, primary_key=True, autoincrement=True)
    create_at = Column(DateTime, default=datetime.now)
    id_mesa = Column(Integer, ForeignKey("mesas.id_mesa"), nullable=False)
    id_user = Column(Integer, ForeignKey("users.id_user"), nullable=False)
    id_actividad = Column(Integer, ForeignKey("actividades.id_actividad"), nullable=True)
    reservation_time = Column(DateTime, nullable=False)
    participants = Column(Integer, nullable=False)