import uuid

from django.db import models
from django.utils.timezone import now


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

    ingredient_id = models.AutoField(
        name="ingredient_id",
        primary_key=True,
        editable=False,
    )
    name = models.CharField(name="name", max_length=80, null=False, unique=True)
    vegetarian = models.BinaryField(name="vegetarian", default=False)
    calories = models.SmallIntegerField(name="calories")
    fat = models.SmallIntegerField(name="fat")
    protein = models.SmallIntegerField(name="protein")
    units = models.CharField(
        name="units",
        choices=UNIT_CHOICES,
        max_length=3,
    )
    create_date = models.DateTimeField(name="create_date", default=now)
    modify_date = models.DateTimeField(name="modify_date", default=now)
