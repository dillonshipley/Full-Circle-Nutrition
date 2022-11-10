import json
import requests
import logging
from datetime import datetime
from time import time
from uuid import UUID, uuid4

import environ
import frontend
import macros_backend
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from recipes.models import Recipe
from recipes.serializers import RecipeSerializer

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()

# Initialize logging helper
log = logging.getLogger("recipes")


# TODO Set up CSRF tokens
@csrf_exempt
@require_http_methods(["GET", "PATCH", "DELETE"])
def recipe_interactions_by_id(request: HttpRequest, recipe_id: UUID) -> JsonResponse:
    """Handles interactions against the recipes model using the recipe_id as a key.
    Uses the request method to determine how the object should be manipulated.

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
@require_http_methods(["POST"])
def create_recipe(request: HttpRequest) -> JsonResponse:
    """Create a new recipe object and persist it to the database

    Args:
        request (HttpRequest): Request containing the new recipe's information
    Returns: Json object containing the status of the request and recipe id of the created recipe
        JsonResponse: 
            201: Created new user
            400: Bad request
    """
    body = json.loads(request.body.decode("utf-8"))

    new_recipe_id = Recipe.objects.create_recipe(
        recipe_name=body["recipe_name"],
        creator=body["creator"],
        price=body["price"],
        meal_type=body["meal_type"],
        description=body["description"],
    )
    return JsonResponse(
        status=201, data={"status": "SUCCESS", "recipe_id": new_recipe_id}
    )


def get_recipe_by_id(recipe_id: UUID) -> JsonResponse:
    """Retrieve a recipe's data using the recipe_id as a query

    Args:
        recipe_id (UUID): UUID of the recipe that should be retrieved from the database
    Returns:
        JsonResponse: Serialized recipe object
            200: Found the recipe object
            404: Recipe could not be found
    """
    result = Recipe.objects.get_recipe_by_id(recipe_id=recipe_id)
    if result is None:
        return JsonResponse(
            status=404, data={"status": "FAILURE", "recipe_id": recipe_id}
        )

    return JsonResponse(
        status=200, data={"result": "SUCCESS", "recipe": result.serialize()}
    )


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
    recipe = Recipe.objects.get_recipe_by_id(recipe_id=recipe_id)
    if recipe is None:
        return JsonResponse(
            status=404, data={"result": "FAILURE", "recipe_id": recipe_id}
        )

    recipe.modify_date = datetime.now()
    validated_data = RecipeSerializer(recipe, data=request, partial=True)
    if validated_data.is_valid():
        # TODO Update the last modified timestamp to the current time (using timezone)
        validated_data.save()
        return JsonResponse(
            status=200, data={"result": "SUCCESS", "recipe_id": recipe_id}
        )

    return JsonResponse(
        status=400,
        data={
            "result": "FAILURE",
            "recipe_id": recipe_id,
        },
    )


def delete_recipe_by_id(recipe_id: UUID) -> JsonResponse:
    """Delete a recipe from the database using the recipe id as a key

    Args:
        recipe_id (UUID): The recipe that should be updated
    Returns:
        JsonResponse: Response indicating the succes of the delete operation
            204: Recipe was deleted successfully
            400: An error prevented the recipe from being deleted
            404: Recipe could not be found
    """
    result = Recipe.objects.delete_recipe_by_id(recipe_id=recipe_id)
    return (
        JsonResponse(status=204, data={"result": "SUCCESS", "recipe_id": recipe_id})
        if result
        else JsonResponse(
            status=404, data={"result": "FAILURE", "recipe_id": recipe_id}
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
