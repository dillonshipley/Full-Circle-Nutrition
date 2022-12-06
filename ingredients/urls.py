from django.urls import path

import ingredients
from .views import create_ingredient, ingredient_interactions_by_id

API_VERSION = f"{ingredients.API_VERSION}"

urlpatterns = [
    path(API_VERSION + "/ingredients/", create_ingredient, name="create_ingredient"),
    path(
        API_VERSION + "/ingredients/<uuid:ingredient_id>/",
        ingredient_interactions_by_id,
        name="ingredient_interactions_by_id",
    ),
]
