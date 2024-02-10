from src.views.http_types.http_response import HttpResponse


def handle_errors(error: Exception) -> HttpResponse:
    return HttpResponse(status_code=400, body={"errors": [{"message": str(error)}]})
