from django.db import models


class Recipe(models.Model):
    recipe_id = models.UUIDField(
        max_length=12,
        primary_key=True,
        unique=True,
        editable=False,
    )
    name = models.CharField(max_length=80, unique=True)
    creator = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField()


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

    name = models.CharField(max_length=80, unique=True)
    vegetarian = models.BinaryField()
    calories = models.SmallIntegerField()
    fat = models.SmallIntegerField()
    protein = models.SmallIntegerField()
    units = models.CharField(
        choices=UNIT_CHOICES,
        max_length=3,
    )
    amount = models.DecimalField(
        decimal_places=2, max_digits=8
    )
    create_date = models.DateTimeField(name="Creation date & time")
    modify_date = models.DateTimeField(name="Last modified date & time")


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
    height = models.DecimalField(decimal_places=2, max_digits=8)
    weight = models.DecimalField(decimal_places=2, max_digits=8)
    body_fat = models.DecimalField(decimal_places=2, max_digits=8)
    goal = models.CharField(choices=GOAL_CHOICES, max_length=3)
    create_date = models.DateTimeField(name="Creation date & time")
    modify_date = models.DateTimeField(name="Last modified date & time")