from django.db import models
from django.utils.timezone import now

import datetime


class Recipe(models.Model):
    recipe_id = models.UUIDField(
        primary_key=True,
        null=False,
        unique=True,
        editable=False,
        default="10000000-0000-0000-0000-000000000000",
    )
    name = models.CharField(max_length=80, null=False, unique=True)
    creator = models.CharField(max_length=80, null=True)
    description = models.CharField(max_length=500, null=True)
    create_date = models.DateTimeField(name="Creation date & time", default=now)
    modify_date = models.DateTimeField(name="Last modified date & time", default=now)


class Ingredient(models.Model):
    UNIT_CHOICES = (
        ("CUP", "cups"),
        ("TBP", "table spoon"),
        ("TSP", "tea spoon"),
        ("DSH", "dash"),
        ("PCH", "pinch"),
        ("LBS", "pound"),
        ("OZS", "ounce"),
        ("GRM", "gram"),
        ("SLC", "slice"),
    )

    ingredient_id = models.UUIDField(
        max_length=12,
        primary_key=True,
        unique=True,
        editable=False,
    )
    name = models.CharField(max_length=80, null=False, unique=True)
    vegetarian = models.BinaryField(default=False)
    calories = models.SmallIntegerField()
    fat = models.SmallIntegerField()
    protein = models.SmallIntegerField()
    units = models.CharField(
        choices=UNIT_CHOICES,
        max_length=3,
    )
    amount = models.DecimalField(decimal_places=2, max_digits=8)
    create_date = models.DateTimeField(name="Creation date & time", default=now)
    modify_date = models.DateTimeField(name="Last modified date & time", default=now)


class User(models.Model):
    GOAL_CHOICES = (
        ("LGN", "low gain"),
        ("MGN", "meduim gain"),
        ("HGN", "high gain"),
    )

    user_id = models.UUIDField(
        max_length=12,
        primary_key=True,
        unique=True,
        editable=False,
    )
    user_name = models.CharField(max_length=25, unique=True)
    height = models.DecimalField(
        decimal_places=2, null=False, max_digits=8, default=0.00
    )
    weight = models.DecimalField(
        decimal_places=2, null=False, max_digits=8, default=0.00
    )
    body_fat = models.DecimalField(
        decimal_places=2, null=False, max_digits=8, default=0.00
    )
    goal = models.CharField(choices=GOAL_CHOICES, null=False, max_length=3)
    create_date = models.DateTimeField(name="Creation date & time", default=now)
    modify_date = models.DateTimeField(name="Last modified date & time", default=now)
