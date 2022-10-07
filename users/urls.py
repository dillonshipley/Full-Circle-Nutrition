from django.urls import path

import users
from users.views import create_user, get_user_by_id

API_VERSION = f"{users.API_VERSION}"

urlpatterns = [
    path(
        API_VERSION + "/users/<uuid:user_id>/",
        get_user_by_id,
        name="get_by_id",
    ),
    path(API_VERSION + "/users/", create_user),
]
