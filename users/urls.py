from django.urls import path

import users
from .views import create_user, user_interactions_by_id

API_VERSION = f"{users.API_VERSION}"

urlpatterns = [
    path(API_VERSION + "/users/", create_user, name="create_user"),
    path(
        API_VERSION + "/users/<uuid:user_id>/",
        user_interactions_by_id,
        name="user_interactions_by_id",
    ),
]
