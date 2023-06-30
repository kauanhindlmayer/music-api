from typing import Type
from src.main.interface.route import RouteInterface
from src.data.use_cases.genre.register import RegisterGenre
from src.presentation.helpers.http_models import HttpRequest, HttpResponse
from src.presentation.errors.http_errors import HttpErrors


class UpdateGenreRouter(RouteInterface):
    """ Class to Define Route to register_genre use case """

    def __init__(self, register_genre_use_case: Type[RegisterGenre]):
        self.register_genre_use_case = register_genre_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ Method to call use case """

        response = None

        if http_request.body and http_request.query:
            # if body and query in htp_request

            body_params = http_request.body.keys()
            query_string_params = http_request.query.keys()

            if ("description" in body_params and "genre_id" in query_string_params):
                # if body and query param contain correct items

                description = http_request.body["description"]
                genre_id = http_request.query["genre_id"]

                response = self.register_genre_use_case.registry(
                    genre_id=genre_id,
                    description=description
                )

            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                https_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=https_error["status_code"], body=https_error["body"]
                )

            return HttpResponse(status_code=201, body=response["Data"])

        # If no body in http_request
        https_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )