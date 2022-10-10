import logging

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
	logger.info(f"{request.body}")
	return JsonResponse(status=201, data={})


@api_view(["GET"])
def get_user_by_id(request) -> JsonResponse:
	"""Retrieve a user from the database using the user_id as a key

	Args:
		request (django.http.request): HTTP request body

	Returns:
		JsonResponse: Reponse containing the queried user information
	"""
	logger.info(f"{request.body}")
	return JsonResponse(data={})


@api_view(["PATCH"])
def patch_user_by_id(request) -> JsonResponse:
	"""_summary_

	Args:
		request (django.http.request): _description_

	Returns:
		JsonResponse: _description_
	"""
	logger.info(f"{request.body}")


@api_view(["DELETE"])
def delete_user_by_id(request) -> JsonResponse:
	"""_summary_

	Args:
		request (django.http.request): _description_

	Returns:
		JsonResponse: _description_
	"""

	logger.info(f"{request.body}")
	return JsonResponse(data={})