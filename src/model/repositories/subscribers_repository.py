from src.model.configs.connection import DBConnectionHandler
from src.model.entities.inscritos import Subscriber
from src.model.repositories.interfaces.subscriber_repository import SubscribeRepositoryInterface


class SubscribersRepository(SubscribeRepositoryInterface):
    def insert(self, subscriber_infos: dict) -> None:
        with DBConnectionHandler() as db:
            try:
                new_subscriber = Subscriber(
                    nome=subscriber_infos.get("nome"),
                    email=subscriber_infos.get("email"),
                    link=subscriber_infos.get("link"),
                    evento_id=subscriber_infos.get("evento_id")
                )
                
                db.session.add(new_subscriber)
                db.session.commit()

            except Exception as exception:
                db.session.rollback()
                raise exception
                  
    def select_subscriber(self, email: str, evento_id: int) -> Subscriber:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(Subscriber)
                .filter(
                    Subscriber.email == email, 
                    Subscriber.evento_id == evento_id
                )
                .one_or_none()
            )

            return data
