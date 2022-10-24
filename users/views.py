import logging

from django.http import JsonResponse
from rest_framework.decorators import api_view

from users.models import User

logger = logging.getLogger("users")


@api_view(["POST"])
def create_user(request) -> JsonResponse:
    """Create user and persist it to the database

    Args:
            request: Request containing the new user's data

    Returns:
            JsonResponse:
    """
    if request.method != "GET":
        pass

    return JsonResponse(data={})


@api_view(["GET"])
def get_user_by_id(request) -> JsonResponse:
    """Retrieve a user from the database using the user_id as a key

    Args:
            request (django.http.request): HTTP request body

    Returns:
            JsonResponse: Reponse containing the queried user information
    """
<<<<<<< Updated upstream
=======
    try:
        user = User.objects.get(user_id=user_id)
        validated_data = UserSerializer(user)
        if not validated_data.is_valid():
            return JsonResponse(status=400, data={"result": "FAILURE", "user_id": user_id, "reason": "Invalid parameters"})
        return JsonResponse(status=200, data={"result": "SUCCESS", "user_id": user_id})
    except User.DoesNotExist as e:
        return JsonResponse(
            status=404, data={"result": "FAILURE", "user_id": user_id, "reason": e}
        )

>>>>>>> Stashed changes

    logger.info(f"{request.body}")
    return JsonResponse(data={})
