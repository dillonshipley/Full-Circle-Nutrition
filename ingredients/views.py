import json
import logging
from uuid import UUID, uuid4

from django.http import HttpRequest, JsonResponse
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Ingredient
from .serializers import IngredientSerializer

log = logging.getLogger("ingredients")


@csrf_exempt
@require_http_methods(["GET", "PATCH", "DELETE"])
def ingredient_interactions_by_id(
    request: HttpRequest, ingredient_id: UUID
) -> JsonResponse:
    """_summary_

    Args:
        request (HttpRequest): _description_
        ingredient_id (UUID): _description_
    Returns:
        JsonResponse: _description_
    """
    if request.method == "GET":
        return get_ingredient_by_id(ingredient_id=ingredient_id)

    if request.method == "PATCH":
        body = json.loads(request.body.decode("utf-8"))
        return patch_ingredient_by_id(ingredient_id=ingredient_id, request=body)

    if request.method == "DELETE":
        return delete_ingredient_by_id(ingredient_id=ingredient_id)

    return JsonResponse(status=405, data={})


@csrf_exempt
@require_http_methods(["POST"])
def create_ingredient(request: HttpRequest) -> JsonResponse:
    """_summary_

    Args:
        request (HttpRequest): _description_
    Returns:
        JsonResponse: _description_
    """
    body = json.loads(request.body.decode("utf-8"))

    status, new_ingredient_or_error = Ingredient.objects.create_ingredient(
        name=body["name"],
        vegetarian=body["vegetarian"],
        calories=body["calories"],
        fat=body["fat"],
        protein=body["protein"],
        units=body["units"],
    )

    if status:
        return JsonResponse(
            status=201,
            data={"status": "SUCCESS", "ingredient_id": new_ingredient_or_error},
        )

    return JsonResponse(
        status=409, data={"status": "FAILURE", "reason": new_ingredient_or_error}
    )


def get_ingredient_by_id(ingredient_id: UUID) -> JsonResponse:
    """_summary_

    Args:
        ingredient_id (UUID): _description_
    Returns:
        JsonResponse: _description_
    """
    exists, ingredient_or_error = Ingredient.objects.get_ingredient_by_id(
        ingredient_id=ingredient_id
    )
    if exists:
        return JsonResponse(
            status=200,
            data={"status": "SUCCESS", "ingredient": ingredient_or_error.serialize()},
        )

    return JsonResponse(
        status=404,
        data={
            "status": "FAILURE",
            "ingredient_id": ingredient_id,
            "reason": ingredient_or_error,
        },
    )


def patch_ingredient_by_id(ingredient_id: UUID, request: dict) -> JsonResponse:
    """_summary_

    Args:
        ingredient_id (UUID): _description_
        request (dict): _description_
    Returns:
        JsonResponse: _description_
    """
    exists, ingredient_or_error = Ingredient.objects.get_ingredient_by_id(
        ingredient_id=ingredient_id
    )
    if not exists:
        return JsonResponse(
            status=404,
            data={
                "status": "FAILURE",
                "ingredient_id": ingredient_id,
                "reason": ingredient_or_error,
            },
        )

    ingredient_or_error.modify_date = now()
    validated_data = IngredientSerializer(
        ingredient_or_error, data=request, partial=True
    )
    if validated_data.is_valid():
        validated_data.save()
        return JsonResponse(
            status=200, data={"status": "SUCCESS", "ingredient_id": ingredient_id}
        )

    return JsonResponse(
        status=400,
        data={
            "status": "SUCCESS",
            "ingredient_id": ingredient_id,
            "reason": "Bad request",
        },
    )


def delete_ingredient_by_id(ingredient_id: UUID) -> JsonResponse:
    """_summary_ad request

    Args:
        ingredient_id (UUID): _description_
    Returns:
        JsonResponse: _description_
    """
    result = Ingredient.objects.delete_ingredients_by_id(ingredient_id=ingredient_id)
    return (
        JsonResponse(200, data={"status": "SUCCESS", "ingredient_id": ingredient_id})
        if result
        else JsonResponse(
            status=404,
            data={
                "status": "FAILURE",
                "ingredient_id": ingredient_id,
                "reason": "Ingredient does not exist",
            },
        )
    )
