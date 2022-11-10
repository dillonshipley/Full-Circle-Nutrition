from datetime import datetime
import json
import logging
from uuid import UUID, uuid4

from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from users.models import User
from users.serializers import UserSerializer

log = logging.getLogger("users")


# TODO Set up CSRF tokens
@csrf_exempt
@require_http_methods(["POST"])
def create_user(request: HttpRequest) -> JsonResponse:
    """Create user and persist it to the database

    Args:
        request(HttpRequest): Request containing the new user's data
    Returns:
        JsonResponse: Response object from the completed request
            201: Successfully created the User object
            400: Bad request
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
def user_interactions_by_id(request: HttpRequest, user_id: UUID) -> JsonResponse:
    """Handles interactions against the user object using the user_id as a key.
    Uses the request method to determine how the object should be manipulated.

    Args:
        request (HttpRequest): Request recieved by the application
        user_id (uuid4): User id of the user model that should be retrieved/altered
    Returns:
        JsonResponse: Reponse object from the completed request
    """
    if request.method == "GET":
        return get_user_by_id(user_id=user_id)

    if request.method == "PATCH":
        body = json.loads(request.body.decode("utf-8"))
        return patch_user_by_id(user_id=user_id, request=body)

    if request.method == "DELETE":
        # TODO Delete user by id method
        return delete_user_by_id(user_id=user_id)

    return JsonResponse(status=405, data={})


def get_user_by_id(user_id: UUID) -> JsonResponse:
    """Return a user's data using the user_id as a query

    Args:
        user_id (uuid4): UUID of the user that should be retrieved from the database
    Returns:
        JsonResponse: Serialized user object
            200: Found the user object
            404: User could not be found
    """
    result = User.objects.get_user_by_id(user_id=user_id)
    if result is not None:
        return JsonResponse(status=404, data={"status": "FAILURE", "user_id": user_id})

    return JsonResponse(
        status=200, data={"result": "SUCCESS", "user": result.serialize()}
    )


def patch_user_by_id(user_id: UUID, request: dict) -> JsonResponse:
    """Update a user using the user_id

    Args:
        user_id (UUID): The user who should be updated
        request (dict): Request body from the PATCH request
    Returns:
        JsonResponse: Response indicating the result of the operation
            200: User was updated successfully
            400: An error prevented the user from being updated
            404: User could not be found
    """
    user = User.objects.get_user_by_id(user_id=user_id)
    if user is None:
        return JsonResponse(status=404, data={"result": "FAILURE", "user_id": user_id})

    user.modify_date = datetime.now()
    validated_data = UserSerializer(user, data=request, partial=True)
    if validated_data.is_valid():
        # TODO Update the last modified timestamp to the current time (using timezone)
        validated_data.save()
        return JsonResponse(status=200, data={"result": "SUCCESS", "user_id": user_id})

    return JsonResponse(
        status=400,
        data={
            "result": "FAILURE",
            "user_id": user_id,
        },
    )


def delete_user_by_id(user_id: UUID) -> JsonResponse:
    """Delete a user from the database using the user id as a key

    Args:
        user_id (uuid4): The user that should be updated
    Returns:
        JsonResponse: Response indicating the success of the operation
            204: User was deleted successfully
            400: An error prevented the user from being deleted
            404: User could not be found
    """
    result = User.objects.delete_user_by_id(user_id=user_id)
    return (
        JsonResponse(status=204, data={"result": "SUCCESS", "user_id": user_id})
        if result
        else JsonResponse(status=404, data={"result": "FAILURE", "user_id": user_id})
    )
