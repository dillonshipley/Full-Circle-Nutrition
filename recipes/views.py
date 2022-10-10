from time import time

import environ
import requests
from django.http import JsonResponse
from users.models import User

import frontend
import macros_backend

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()


def index(request) -> JsonResponse:
    """Return a generic response

    Returns
        JsonResponse: Generic response
    """
    return JsonResponse(data={"response": "Thanks for hitting the recipes api index!"})


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
