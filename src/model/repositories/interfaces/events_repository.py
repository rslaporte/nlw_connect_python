from abc import ABC, abstractmethod
from src.model.entities.eventos import Event

class EventsRepositoryInterface(ABC):
    
    @abstractmethod
    def insert(self, event_name: str) -> None: pass
            
    @abstractmethod            
    def select_event(self, event_name: str) -> Event: pass
