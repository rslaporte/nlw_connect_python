from src.model.configs.connection import DBConnectionHandler
from src.model.entities.eventos import Event
from src.model.repositories.interfaces.events_repository import EventsRepositoryInterface

class EventsRepository(EventsRepositoryInterface):
    def insert(self, event_name: str) -> None:
        with DBConnectionHandler() as db:
            try:
                new_event = Event(nome=event_name)
                db.session.add(new_event)
                db.session.commit()

            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def select_event(self, event_name: str) -> Event:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(Event)
                .filter(Event.nome == event_name)
                .one_or_none()
            )

            return data
