import pytest
from .events_link_repository import EventsLinkRepository

@pytest.mark.skip("Insert in DB")
def test_insert_eventos_link():
    event_id = 12
    subs_id = 18
    event_repo = EventsLinkRepository()

    event_repo.insert(event_id, subs_id)

@pytest.mark.skip("Select in DB")
def test_select_event():
    event_name = "eventoTeste"
    event_repo = EventsLinkRepository()

    event = event_repo.select_event(event_name)
    print(event)
    print(event.nome)
