import json
import logging
from uuid import uuid4

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from users.models import User

logger = logging.getLogger("users")


# TODO Set up CSRF tokens
@csrf_exempt
@require_http_methods(["POST"])
def create_user(request) -> JsonResponse:
    """Create user and persist it to the database

    Args:
        request(django.http.request): Request containing the new user's data
    Returnsuser_id:
        JsonResponse:
    """
    body = json.loads(request.body.decode("utf-8"))
    
    new_user = User(
        user_name=body["user_name"],
        age=body["age"],
        height=body["height"],
        weight=body["weight"],
        body_fat=body["body_fat"],
        goal=body["goal"],
    ).clean()
    return JsonResponse(status=201, data={"status": "SUCCESS", "user_id": new_user.id})


@csrf_exempt
@require_http_methods(["GET", "PATCH", "DELETE"])
def user_interactions_by_id(request, user_id) -> JsonResponse:
    """Handles interactions against the user object using the user_id as a key.
    Uses the request body to

    Args:
        request (django.http.request): HTTP request body
    Returns:
        JsonResponse: Reponse containing the queried user information
    """
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
        user_id (uuid4): UUID of the user that should be retrieved from the database
    Returns:
        JsonResponse: Serialized user object
    """
    try:
        result = User.objects.get_user_by_id(user_id=user_id)
        return JsonResponse(
            status=200, data={"result": "SUCCESS", "user": result.serialize()}
        )
    except User.DoesNotExist as e:
        return JsonResponse(
            status=404, data={"status": "FAILURE", "user_id": user_id, "reason": e}
        )


def patch_user_by_id(user_id: uuid4) -> JsonResponse:
    """_summary_

    Args:
        user_id (uuid): _description_

    Returns:
        JsonResponse: _description_
    """
    pass


def delete_user_by_id(user_id: uuid4) -> JsonResponse:
    """Delete a user from the database using the user id as a key

    Args:
        user_id (uuid4): _description_
    Returns:
        JsonResponse: _description_
    """
    try:
        result = User.objects.filter(user_id=user_id).delete()
        return JsonResponse(
            status=204, data={"result": "SUCCESS", "user_id": user_id, "data": result}
        )
    except User.DoesNotExist as e:
        return JsonResponse(
            status=404, data={"result": "FAILURE", "user_ud": user_id, "reason": e}
        )
