from typing import Type
from src.main.interface.route import RouteInterface
from src.data.use_cases.genre.find import FindGenre
from src.presentation.helpers.http_models import HttpResponse, HttpRequest
from src.presentation.errors.http_errors import HttpErrors


class FindGenreRouter(RouteInterface):
    """ Class to define Route to find_genre use case """

    def __init__(self, find_genre_use_case: Type[FindGenre]):
        self.find_genre_use_case = find_genre_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ Method to call use case """

        response = None

        if http_request.query:
            # if query in http_request

            query_string_params = http_request.query.keys()

            if "genre_id" in query_string_params:
                genre_id = http_request.query["genre_id"]
                response = self.find_genre_use_case.by_genre_id(
                    genre_id=genre_id
                )
            elif "description" in query_string_params:
                description = http_request.query["description"]
                response = self.find_genre_use_case.by_description(
                    description=description
                )
            else:
                response = {"Success": False, "Data": None}

        else:
            # if no query in http_request
            response = self.find_genre_use_case.find()

        if response["Success"] is False:
            https_error = HttpErrors.error_400()
            return HttpResponse(
                status_code=https_error["status_code"], body=https_error["body"]
            )
        
        return HttpResponse(status_code=200, body=response["Data"])