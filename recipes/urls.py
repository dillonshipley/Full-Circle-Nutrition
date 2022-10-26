from django.urls import path

import recipes
from recipes.views import create_recipe, recipe_interactions_by_id, health

API_VERSION = f"{recipes.API_VERSION}"

urlpatterns = [
    path(API_VERSION + "/recipes/", create_recipe, name="create_recipe"),
    path(
        API_VERSION + "/recipes/<uuid:recipe_id>/",
        recipe_interactions_by_id,
        name="recipe_interactions_by_id",
    ),
    path("health/", health, name="health"),
]
