import logging
from uuid import uuid4

from django.http import JsonResponse
from rest_framework.decorators import api_view

from users.models import User

logger = logging.getLogger("users")


@api_view(["POST"])
def create_user(request) -> JsonResponse:
	"""Create user and persist it to the database

	Args:
		request(django.http.request): Request containing the new user's data

	Returns:
		JsonResponse:
	"""
	# TODO Post user method
	logger.info(f"{request.body}")
	return JsonResponse(status=201, data={})


@api_view(["GET", "POST", "PATCH"])
def user_interactions_by_id(request) -> JsonResponse:
	"""Handles interactions against the user object using the user_id as a key.
	Uses the request body to 

	Args:
		request (django.http.request): HTTP request body

	Returns:
		JsonResponse: Reponse containing the queried user information
	"""
	# TODO Check that the user exists before trying to send the request further
	logger.info(f"{request.body}")

	user_id = uuid4()

	if request.GET:
		return get_user_by_id(user_id=user_id) 

	if request.PATCH:
		# TODO Patch user by id method
		pass		

	if request.DELETE:
		# TODO Delete user by id method
		pass

	logger.info(f"{request.body}")
	return JsonResponse(data={})

def get_user_by_id(user_id: uuid4) -> JsonResponse:
	"""Return a user's data 

	Args:
		request (uuid4): _description_

	Returns:
		JsonResponse: _description_
	"""
	result = User.objects.get(pk=user_id)
	return JsonResponse(data={})
