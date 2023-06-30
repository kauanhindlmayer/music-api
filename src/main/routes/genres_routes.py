from flask import jsonify, Blueprint, request
from src.main.adapter.router_adapter import flask_adapter
from src.main.composer.genre.find_genre_composite import find_genre_composer
from src.main.composer.genre.register_genre_composite import register_genre_composer
from src.main.composer.genre.update_genre_composite import update_genre_composer
from src.main.composer.genre.delete_genre_composite import delete_genre_composer

api_routes_bp = Blueprint("api_routes", __name__)

@api_routes_bp.route("/api/genres", methods=["GET"])
def get_genre():
    """ get genre route """

    response = flask_adapter(request=request, api_route=find_genre_composer())

    message = []
    if response.status_code < 300:
        # If not error, format the message and return it

        for element in response.body:
            message.append(
                {
                    "type": "Genres",
                    "id": element.id,
                    "attributes": {"description": element.description},
                }
            )

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return (
        jsonify(
            {
                "error": {
                    "status": response.status_code,
                    "title": response.body["error"],
                }
            }
        ),
        response.status_code,
    )

@api_routes_bp.route("/api/genres", methods=["POST"])
def register_genre():
    """ register genre route """

    message = {}
    response = flask_adapter(request=request, api_route=register_genre_composer())

    if response.status_code < 300:
        # If not error, format the message and return it

        message = {
            "type": "Users",
            "id": response.body.id,
            "attributes": {"name": response.body.name},
        }

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return (
        jsonify(
            {
                "error": {
                    "status": response.status_code,
                    "title": response.body["error"],
                }
            }
        ),
        response.status_code,
    )

@api_routes_bp.route("/api/genres", methods=["PUT"])
def update_genre():
    """ update genre route """

    message = {}
    response = flask_adapter(request=request, api_route=update_genre_composer())

    if response.status_code < 300:
        # If not error, format the message and return it

        message = {
            "type": "Users",
            "id": response.body.id,
            "attributes": {"name": response.body.name},
        }

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return (
        jsonify(
            {
                "error": {
                    "status": response.status_code,
                    "title": response.body["error"],
                }
            }
        ),
        response.status_code,
    )

@api_routes_bp.route("/api/genres", methods=["DELETE"])
def delete_genre():
    """ delete genre route """

    message = {}
    response = flask_adapter(request=request, api_route=delete_genre_composer())

    if response.status_code < 300:
        # If not error, format the message and return it

        message = {
            "type": "Users",
            "id": response.body.id,
            "attributes": {"name": response.body.name},
        }

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return (
        jsonify(
            {
                "error": {
                    "status": response.status_code,
                    "title": response.body["error"],
                }
            }
        ),
        response.status_code,
    )

