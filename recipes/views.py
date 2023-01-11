import json
import logging
from time import time
from uuid import UUID

import environ
import requests
from django.http import HttpRequest, JsonResponse, QueryDict
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

import frontend
import macros_backend
from .models import Recipe
from .serializers import RecipeSerializer

env = environ.Env()
environ.Env.read_env()

log = logging.getLogger("recipes")


# TODO Set up CSRF tokens
@csrf_exempt
@require_http_methods(["GET", "PATCH", "DELETE"])
def recipe_interactions_by_id(request: HttpRequest, recipe_id: UUID) -> JsonResponse:
    """Handles interactions against the recipes model using the recipe_id as a key.
    Uses the request method to determine how the request should be handled

    Args:
        request (HttpRequest): Request recieved by the application
        recipe_id (uuid4): Recipe id of the recipe model that should be retrieved/altered
    Returns:
        JsonResponse: Response object from the completed request
    """
    if request.method == "GET":
        return get_recipe_by_id(recipe_id=recipe_id)

    if request.method == "PATCH":
        body = json.loads(request.body.decode("utf-8"))
        return patch_recipe_by_id(recipe_id=recipe_id, request=body)

    if request.method == "DELETE":
        return delete_recipe_by_id(recipe_id=recipe_id)

    return JsonResponse(status=405, data={})

@csrf_exempt
@require_http_methods(['GET', "POST"])
def recipe_interactions(request: HttpRequest) -> JsonResponse:
    """Handle interactions against the recipes model. Uses the request method to determine
    how the request should be handled

    Args:
        request (HttpRequest): Request recieved by the application
    Returns:
        JsonResponse: Response object for the completed request
    """
    if request.method == 'POST':
        request_body = json.loads(request.body.decode('utf-8'))
        return create_recipe(request_body)

    if request.method == 'GET':
        query_params = request.GET
        return get_recipe_by_filters(query_params)

    return JsonResponse(status=405, data={})


def create_recipe(request_body: dict) -> JsonResponse:
    """Create a new recipe object and persist it to the database

    Args:
        request (HttpRequest): Request containing the new recipe's information
    Returns: Json object containing the status of the request and recipe id of the created recipe
        JsonResponse:
            201: Created new user
            400: Bad request
    """
    status, result = Recipe.objects.create_recipe(
        recipe_name=request_body["recipe_name"],
        creator=request_body["creator"],
        price=request_body["price"],
        meal_type=request_body["meal_type"],
        description=request_body["description"],
    )

    if status:
        return JsonResponse(status=201, data={"status": "SUCCESS", "recipe_id": result})

    return JsonResponse(status=409, data={"status": "FAILURE", "reason": result})


@csrf_exempt
@require_http_methods(["GET"])
def get_all_recipes(request: HttpRequest) -> JsonResponse:
    status, result = Recipe.objects.get_recipes()

    if status:
        return JsonResponse(
            status=200,
            data={
                "status": "SUCCESS",
                "data": {
                    index: recipe.serialize() for index, recipe in enumerate(result)
                },
            },
        )

    return JsonResponse(status=404, data={"status": "FAILURE", "reason": str(result)})


def get_recipe_by_id(recipe_id: UUID) -> JsonResponse:
    """Retrieve a recipe's data using the recipe_id as a query

    Args:
        recipe_id (UUID): UUID of the recipe that should be retrieved from the database
    Returns:
        JsonResponse: Serialized recipe object
            200: Found the recipe object
            404: Recipe could not be found
    """
    status, result = Recipe.objects.get_recipe_by_id(recipe_id=recipe_id)
    if status:
        return JsonResponse(
            status=200, data={"status": "SUCCESS", "recipe": result.serialize()}
        )

    return JsonResponse(
        status=404,
        data={"status": "FAILURE", "recipe_id": recipe_id, "reason": str(result)},
    )

def get_recipe_by_filters(query_params: QueryDict) -> JsonResponse:
    log.info(f"Query Params: {query_params}")
    is_valid, filter_values_or_error = validator.validate(query_params)
    if is_valid:
        filter_results = Recipe.objects


def patch_recipe_by_id(recipe_id: UUID, request: dict) -> JsonResponse:
    """Update a recipe using the recipe_id

    Args:
        recipe_id (UUID): The recipe who should be updated
        request (dict): Request body from the PATCH request
    Returns:
        JsonResponse: Response indicating the result of the operation
            200: Recipe was update successfully
            400: An error prevented the recipe from being updated
            404: Recipe could not be found
    """
    exists, recipe_or_error = Recipe.objects.get_recipe_by_id(recipe_id=recipe_id)
    if not exists:
        return JsonResponse(
            status=404,
            data={
                "status": "FAILURE",
                "recipe_id": recipe_id,
                "reason": recipe_or_error,
            },
        )

    recipe_or_error.modify_date = now()
    validated_data = RecipeSerializer(recipe_or_error, data=request, partial=True)
    if validated_data.is_valid():
        validated_data.save()
        return JsonResponse(
            status=200, data={"status": "SUCCESS", "recipe_id": recipe_id}
        )

    return JsonResponse(
        status=400,
        data={"status": "FAILURE", "recipe_id": recipe_id, "reason": "Bad request"},
    )


def delete_recipe_by_id(recipe_id: UUID) -> JsonResponse:
    """Delete a recipe from the database using the recipe id as a key

    Args:
        recipe_id (UUID): The recipe that should be deleted
    Returns:
        JsonResponse: Response indicating the succes of the delete operation
            200: Recipe was deleted successfully
            404: Recipe could not be found
    """
    result = Recipe.objects.delete_recipe_by_id(recipe_id=recipe_id)
    return (
        JsonResponse(status=200, data={"status": "SUCCESS", "recipe_id": recipe_id})
        if result
        else JsonResponse(
            status=404,
            data={
                "status": "FAILURE",
                "recipe_id": recipe_id,
                "reason": "Recipe does not exist",
            },
        )
    )


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
