from flask import Blueprint, jsonify, request

events_link_route_bp = Blueprint("events_link_route", __name__)

from src.controllers.events_link.events_link_creator import EventsLinkCreator
from src.model.repositories.events_link_repository import EventsLinkRepository
from src.https_types.http_request import HttpRequest

@events_link_route_bp.route("/events_link", methods=["POST"])
def create_new_event():
    events_link_repo = EventsLinkRepository()
    events_link_creator = EventsLinkCreator(events_link_repo)

    http_request = HttpRequest(body=request.json)
    http_response = events_link_creator.create(http_request)

    return jsonify(http_response.body), http_response
