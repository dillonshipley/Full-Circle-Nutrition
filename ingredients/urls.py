from django.urls import path

import ingredients
from .views import (
    ingredient_interactions_by_id,
    get_all_ingredients,
    ingredient_interactions,
)

API_VERSION = f"{ingredients.API_VERSION}"

urlpatterns = [
    path(
        API_VERSION + "/ingredients/", ingredient_interactions, name="Ingredient Interactions"
    ),
    path(
        API_VERSION + "/ingredients/all/",
        get_all_ingredients,
        name="get_all_ingredients",
    ),
    path(
        API_VERSION + "/ingredients/<uuid:ingredient_id>/",
        ingredient_interactions_by_id,
        name="ingredient_interactions_by_id",
    ),
]
