import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip("Insert in DB")
def test_insert():
    subscriber_infos = {
        "nome": "meuNome",
        "email": "email@email.com",
        "evento_id": 1
    }

    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_infos)

@pytest.mark.skip("Selecting in DB")
def test_select_subscriber():
    email = "email@email.com"
    evento_id = 1

    subs_repo = SubscribersRepository()
    res = subs_repo.select_subscriber(email, evento_id)
    print(res.nome)

@pytest.mark.skip("Get Ranking of each link")
def test_get_ranking():
    event_id = 3
    subs_repo = SubscribersRepository()
    resp = subs_repo.get_ranking(event_id)
    print()

    for elem in resp:
        print(f"Link: {elem.link}, total de inscritos: {elem.total}")