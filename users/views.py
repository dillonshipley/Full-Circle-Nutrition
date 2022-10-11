import json
import logging
from uuid import uuid4

from django.http import JsonResponse

from users.models import User

logger = logging.getLogger("users")


def create_user(request) -> JsonResponse:
    """Create user and persist it to the database

    Args:
            request(django.http.request): Request containing the new user's data

    Returns:
            JsonResponse:
    """
    # TODO Post user method
    body = json.loads(request.body.decode("utf-8"))
    new_user = User(
        user_name=body["user_name"],
        age=body["age"],
        height=body["height"],
        weight=body["weight"],
        body_fat=body["body_fat"],
        goal=body["goal"],
    ).save()
    return JsonResponse(status=201, data={"status": "SUCCESS"})


def user_interactions_by_id(request, user_id) -> JsonResponse:
    """Handles interactions against the user object using the user_id as a key.
    Uses the request body to

    Args:
            request (django.http.request): HTTP request body

    Returns:
            JsonResponse: Reponse containing the queried user information
    """
    # TODO Check that the user exists before trying to send the request further
    logger.info(f"{request.path}")

    user_id = uuid4()

    if request.method == "GET":
        return get_user_by_id(user_id=user_id)

    if request.method == "PATCH":
        # TODO Patch user by id method
        pass

    if request.method == "DELETE":
        # TODO Delete user by id method
        pass

    logger.info(f"{request.body}")
    return JsonResponse(data={})


def get_user_by_id(user_id: uuid4) -> JsonResponse:
    """Return a user's data

    Args:
        user_id (uuid4): _description_

    Returns:
        JsonResponse: _description_
    """
    try:
        print(f"{user_id}")
        result = User.objects.get(pk=user_id)
        return JsonResponse(status=200, data={})
    except User.DoesNotExist:
        return JsonResponse(status=404, data={'status': "DOES NOT EXIST"})

    
