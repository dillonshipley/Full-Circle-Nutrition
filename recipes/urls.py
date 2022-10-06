from django.urls import path

import recipes
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("health/", views.health, name="health"),
	path(
		f"{recipes.API_VERSION}/users/<uuid:user_id>/",
		views.get_user_by_id,
		name="get_by_id",
	),
]
