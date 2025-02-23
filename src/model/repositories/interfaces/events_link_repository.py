from abc import ABC, abstractmethod
from src.model.entities.events_link import EventsLink

class EventsLinkRepositoryInterface():
    @abstractmethod
    def insert(self, event_id: int, subscriber_id: int) -> None: pass
       
    @abstractmethod
    def select_events_link(self, event_id: int, subscriber_id: int) -> EventsLink: pass
       