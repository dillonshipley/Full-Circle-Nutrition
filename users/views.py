import json
import logging
from uuid import uuid4

from django.http import JsonResponse, request
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from users.models import User
from users.serializers import UserSerializer

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

    new_user_id = User.objects.create_user(
        user_name=body["user_name"],
        age=body["age"],
        height=body["height"],
        weight=body["weight"],
        body_fat=body["body_fat"],
        goal=body["goal"],
    )
    return JsonResponse(status=201, data={"status": "SUCCESS", "user_id": new_user_id})


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
        return patch_user_by_id(user_id=user_id, request=request.body)

    if request.method == "DELETE":
        # TODO Delete user by id method
        pass


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


def patch_user_by_id(user_id: uuid4, request: dict) -> JsonResponse:
    """Update a user using the user_id

    Args:
        user_id (uuid4): The user who should be updated
        request (request): Request body from the PATCH request

    Returns:
        JsonResponse: Response indicating the result of the operation
            200: User was updated successfully
            400: An error prevented the user from being updated
            404: User could not be found
    """
    try:
        user = User.objects.get(user_id=user_id)
        validated_data = UserSerializer(user)
        if not validated_data.is_valid():
            return JsonResponse(status=400, data={"result": "FAILURE", "user_id": user_id, "reason": })
        return JsonResponse(status=200, data={"result": "SUCCESS", "user_id": user_id})
    except User.DoesNotExist as e:
        return JsonResponse(
            status=404, data={"result": "FAILURE", "user_id": user_id, "reason": e}
        )


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
