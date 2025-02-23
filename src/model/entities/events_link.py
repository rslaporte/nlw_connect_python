from src.model.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey

class EventsLink(Base):
    __tablename__ = "Eventos_link"

    id = Column(Integer, primary_key=True, autoincrement=True)
    evento_id = Column(Integer, ForeignKey("Events.id"), nullable=False)
    inscrito_id = Column(Integer, ForeignKey("Subscribers.id"), nullable=False)
    link = Column(String, nullable=False)