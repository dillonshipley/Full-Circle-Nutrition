from django.urls import path

import recipes
from recipes.views import (
    create_recipe,
    recipe_interactions_by_id,
    get_all_recipes,
    health,
)

API_VERSION = f"{recipes.API_VERSION}"

urlpatterns = [
    path("health/", health, name="health"),
    path(API_VERSION + "/recipes/", create_recipe, name="create_recipe"),
    path(API_VERSION + "/recipes/all/", get_all_recipes, name="get_all_recipes"),
    path(
        API_VERSION + "/recipes/<uuid:recipe_id>/",
        recipe_interactions_by_id,
        name="recipe_interactions_by_id",
    ),
]
