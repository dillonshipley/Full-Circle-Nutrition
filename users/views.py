import json
import logging
from uuid import UUID, uuid4

from django.http import HttpRequest, JsonResponse
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from users.models import User
from users.serializers import UserSerializer

log = logging.getLogger("users")


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
        return delete_user_by_id(user_id=user_id)

    return JsonResponse(status=405, data={})


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

    status, new_user_or_error = User.objects.create_user(
        user_name=body["user_name"],
        age=body["age"],
        height=body["height"],
        weight=body["weight"],
        body_fat=body["body_fat"],
        goal=body["goal"],
    )
    if status:
        return JsonResponse(
            status=201, data={"status": "SUCCESS", "user_id": new_user_or_error}
        )

    return JsonResponse(
        status=409, data={"status": "FAILURE", "reason": new_user_or_error}
    )


def get_user_by_id(user_id: UUID) -> JsonResponse:
    """Return a user's data using the user_id as a query

    Args:
        user_id (uuid4): UUID of the user that should be retrieved from the database
    Returns:
        JsonResponse: Serialized user object
            200: Found the user object
            404: User could not be found
    """
    exists, user_or_error = User.objects.get_user_by_id(user_id=user_id)
    if exists:
        return JsonResponse(
            status=200, data={"status": "SUCCESS", "user": user_or_error.serialize()}
        )

    return JsonResponse(
        status=404,
        data={"status": "FAILURE", "user_id": user_id, "reason": str(user_or_error)},
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
    exists, user_or_error = User.objects.get_user_by_id(user_id=user_id)
    if not exists:
        return JsonResponse(
            status=404,
            data={"status": "FAILURE", "user_id": user_id, "reason": user_or_error},
        )

    user_or_error.modify_date = now()
    validated_data = UserSerializer(user_or_error, data=request, partial=True)
    if validated_data.is_valid():
        validated_data.save()
        return JsonResponse(status=200, data={"status": "SUCCESS", "user_id": user_id})

    return JsonResponse(
        status=400,
        data={"status": "FAILURE", "user_id": user_id, "reason": "Bad request"},
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
        JsonResponse(status=200, data={"status": "SUCCESS", "user_id": user_id})
        if result
        else JsonResponse(status=404, data={"status": "FAILURE", "user_id": user_id})
    )
