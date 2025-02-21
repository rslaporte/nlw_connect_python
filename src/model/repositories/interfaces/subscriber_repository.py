from abc import ABC, abstractmethod
from src.model.entities.inscritos import Subscriber

class SubscribeRepositoryInterface:

    @abstractmethod
    def insert(self, subscriber_info: dict) -> None: pass
            
    @abstractmethod
    def select_sub(self, subscriver_email: str, evento_id: int) -> Subscriber: pass