from django.urls import path

import recipes
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("health/", views.health, name="health"),
]
