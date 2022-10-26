import uuid

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils.timezone import now


class RecipeManager(models.Manager):
    def create_recipe(
        self,
        recipe_name: str,
        creator: str,
        price: float,
        meal_type: str,
        description: str
    ) -> uuid:
        """Creates and validates new recipe entries to the database. Returns the UUID of the new recipe

        Args:
            recipe_name (str): _description_
            creator (str): _description_
            price (float): _description_
            meal_type (str): _description_
            description (str): _description_

        Returns:
            uuid: _description_
        """
        self.create(
            recipe_name=recipe_name,
            creator=creator,
            price=price,
            meal_type=meal_type,
            description=description
        ).clean()
        return self.last().user_id
    def get_recipe_by_id(self, recipe_id: uuid):
        try:
            return self.get(recipe_id=recipe_id)
        except ObjectDoesNotExist:
            return None

class Recipe(models.Model):
    meal_type_options = (
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
        default=uuid.uuid4(),
    )
    recipe_name = models.CharField(name="recipe_name", max_length=80, null=False, unique=True)
    creator = models.CharField(name="creator", max_length=80, null=True)
    price = models.DecimalField(
        name="price", decimal_places=2, max_digits=10, default=0.00
    )
    meal_type = models.CharField(
        name="meal_type", choices=meal_type_options, max_length=2, null=True
    )
    description = models.CharField(name="description", max_length=500, null=True)
    create_date = models.DateTimeField(name="create_date", editable=False, default=now)
    modify_date = models.DateTimeField(name="modify_date", default=now)
