from uuid import UUID, uuid4

from django.db import models
from django.utils.timezone import now

from .managers import RecipeManager


class Recipe(models.Model):
    __meal_type_options = (
        ("BF", "Breakfast"),
        ("LC", "Lunch"),
        ("DN", "Dinner"),
        ("SK", "Snack"),
    )

    recipe_id = models.UUIDField(
        name="recipe_id",
        primary_key=True,
        max_length=36,
        null=False,
        unique=True,
        editable=False,
        default=uuid4(),
    )
    recipe_name = models.CharField(
        name="recipe_name", max_length=80, null=False, unique=True, default="Recipe"
    )
    creator = models.CharField(name="creator", max_length=80, null=True)
    price = models.DecimalField(
        name="price", decimal_places=2, max_digits=10, default=0.00
    )
    meal_type = models.CharField(
        name="meal_type", choices=__meal_type_options, max_length=2, null=True
    )
    description = models.CharField(name="description", max_length=500, null=True)
    create_date = models.DateTimeField(name="create_date", editable=False, default=now)
    modify_date = models.DateTimeField(name="modify_date", default=now)

    objects = RecipeManager()

    @property
    def id(self) -> UUID:
        return self.recipe_id

    def serialize(self) -> dict:
        """Custom serializer for the Recipe class

        Returns:
            dict: Recipe serialization
        """
        return {
            "recipe_id": (self.recipe_id),
            "recipe_name": self.recipe_name,
            "creator": self.creator,
            "price": float(self.price),
            "meal_type": self.get_meal_type_display(),
            "description": self.description,
            "create_date": self.create_date,
            "modify_date": self.modify_date,
        }

    def __str__(self) -> str:
        return f"{self.meal_type}({self.recipe_name}, {self.creator}): {self.recipe_id}"
