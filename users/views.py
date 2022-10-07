import logging
from django.http import JsonResponse
from rest_framework.decorators import api_view

from users.models import User

logger = logging.getLogger("users")

@api_view(['POST'])
def create_user(request) -> JsonResponse:
    """Create user and persist it to the database

    Args:
            request: Request containing the new user's data

    Returns:
            JsonResponse:
    """
    if request.method != 'GET':
        pass


    user = User(user)

    return JsonResponse(data={})


@api_view(['GET'])
def get_user_by_id(request) -> JsonResponse:
	"""Retrieve a user from the database using the user_id as a key

	Args:
		request (django.http.request): HTTP request body 

	Returns:
		JsonResponse: Reponse containing the queried user information
	"""

	logger.info(f"{request.body}")
	return JsonResponse(data={})
