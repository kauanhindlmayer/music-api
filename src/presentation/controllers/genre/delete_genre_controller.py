from typing import Type
from src.main.interface.route import RouteInterface
from src.data.use_cases.genre.delete import DeleteGenre
from src.presentation.helpers.http_models import HttpResponse, HttpRequest
from src.presentation.errors.http_errors import HttpErrors


class DeleteGenreRouter(RouteInterface):
    """ Class to define Route to delete_genre use case """

    def __init__(self, delete_genre_use_case: Type[DeleteGenre]):
        self.delete_genre_use_case = delete_genre_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ Method to call use case """

        response = None

        if http_request.query:
            # if query in http_request

            query_string_params = http_request.query.keys()

            if "genre_id" in query_string_params:
                genre_id = http_request.query["genre_id"]
                response = self.delete_genre_use_case.by_genre_id(
                    genre_id=genre_id
                )
            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                https_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=https_error["status_code"], body=https_error["body"]
                )
            
            return HttpResponse(status_code=200, body=response["Data"])

        # If no query in http_request
        https_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )