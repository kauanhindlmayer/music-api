from typing import Type
from sqlalchemy.exc import IntegrityError
from src.presentation.helpers.http_models import HttpRequest, HttpResponse
from src.presentation.errors.http_errors import HttpErrors
from src.main.interface.route import RouteInterface as Route


def flask_adapter(request: any, api_route: Type[Route]) -> any:
    """Adapter pattern to Flask
    :param - Flask Request
    :api_route: Composite Routes
    """

    try:
        # Query string params
        query_string_params = request.args.to_dict()

        # Formating information
        if "genre_id" in query_string_params.keys():
            query_string_params["genre_id"] = int(query_string_params["genre_id"])

    except:
        https_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )

    # request.json
    http_request = HttpRequest(
        header=request.headers, body=request, query=query_string_params
    )

    try:
        response = api_route.route(http_request)

    except IntegrityError:
        https_error = HttpErrors.error_409()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )
    except:
        https_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )
    return response