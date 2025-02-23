from abc import ABC, abstractmethod
from src.model.entities.subscribers import Subscribers

class SubscriberRepositoryInterface:

    @abstractmethod
    def insert(self, subscriber_info: dict) -> None: pass
            
    @abstractmethod
    def select_sub(self, subscriver_email: str, event_id: int) -> Subscribers: pass

    @abstractmethod
    def select_subscribers_by_link(self, link: str, event_id: int) -> Subscribers: pass

    @abstractmethod
    def get_ranking(self, event_id: int) -> list: pass
