from sqlalchemy import func, desc
from src.model.configs.connection import DBConnectionHandler
from src.model.entities.subscribers import Subscribers
from src.model.repositories.interfaces.subscriber_repository import SubscriberRepositoryInterface


class SubscribersRepository(SubscriberRepositoryInterface):
    def insert(self, subscriber_infos: dict) -> None:
        with DBConnectionHandler() as db:
            try:
                new_subscriber = Subscribers(
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
                  
    def select_subscriber(self, email: str, event_id: int) -> Subscribers:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(Subscriber)
                .filter(
                    Subscriber.email == email, 
                    Subscriber.evento_id == event_id
                )
                .one_or_none()
            )

            return data
        
    def select_subscribers_by_link(self, link: str, event_id: int) -> Subscribers:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(Subscribers)
                .filter(
                    Subscribers.evento_id == event_id,
                    Subscribers.link == link
                )
                .all()
            )
        
        return data

    def get_ranking(self, event_id: int) -> list:
        with DBConnectionHandler() as db:
            result = (
                db.session
                .query(
                    Subscribers.link,
                    func.count(Subscribers.id).label("total")
                )
                .filter(
                    Subscribers.evento_id == event_id,
                    Subscribers.link.isnot(None)
                )
                .group_by(Subscribers.link)
                .order_by(desc("total"))
                .all()
            )

            return result