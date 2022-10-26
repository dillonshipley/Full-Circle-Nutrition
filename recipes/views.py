from datetime import datetime
from time import time
from uuid import uuid4

import environ
import frontend
import macros_backend
import requests
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from recipes.models import Recipe

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()

# TODO Set up CSRF tokens
@csrf_exempt
@require_http_methods(["GET", "PATCH", "DELETE"])
def user_interactions_by_id(request: HttpRequest, recipe_id: uuid4) -> JsonResponse:
    """Handles interactions against the recipes model using the recipe_id as a key. 
    Uses the request method to determine how the object should be manipulated.

    Args:
        request (HttpRequest): Request recieved by the application
        recipe_id (uuid4): Recipe id of the recipe model that should be retrieved/altered 
    Returns:
        JsonResponse: Response object from the completed request
    """
    if request.method == "GET":
        pass

    if request.method == "PATCH":
        pass

    if request.method == "DELETE":
        pass

    else:
        return JsonResponse(status=405, data={})

@csrf_exempt
@require_http_methods(["POST"])
def create_recipe(request: HttpRequest) -> JsonResponse: 
    pass


def health(request) -> JsonResponse:
    """Return a response that describes the status of the application, and other related services

    Returns
        JsonResponse: Health response describing status of the application
    """
    response_content = dict()

    # Add information about the current application
    response_content.setdefault(
        "macros_back_end",
        {
            "status": "UP",
            "version": macros_backend.VERSION,
            "timestamp": time(),
            "uptime": time() - macros_backend.START_TIME,
            "message": "Backend service running",
        },
    )

    # TODO Ping the database to see if its up
    response_content.setdefault(
        "macros_db",
        {
            "status": "DOWN",
            "version": macros_backend.VERSION,
            "timestamp": time(),
            "message": "No response from the database. Has the service been started? Is the cluster active?",
        },
    )

    # Ping the front end webapp to see if the service is running
    try:
        res = requests.get(env("FRONT_END_URL"), timeout=0.1)
        # Got a response from the front end, add field to response noting the service is up
        response_content.setdefault(
            "macros_front_end",
            {
                "status": "UP",
                "version": frontend.VERSION,
                "timestamp": time(),
            },
        )
    except requests.exceptions.ConnectionError:
        # No response from the front end, add field to response noting the service is down
        response_content.setdefault(
            "macros_front_end",
            {
                "status": "DOWN",
                "version": frontend.VERSION,
                "timestamp": time(),
                "message": "No response from the front end. Has the service been started?",
            },
        )

    response = {"services": response_content}
    return JsonResponse(data=response)
