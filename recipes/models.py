from uuid import UUID, uuid4

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
        description: str,
    ) -> UUID:
        """Creates and validates new recipe entries to the database. Returns the UUID of the new recipe

        Args:
            recipe_name (str): Name of the recipe that should be created
            creator (str): Creator of the new recipe
            price (float): Total price of the recipe
            meal_type (str): Meal type enum value
            description (str): Description of the new meal

        Returns:
            uuid: UUID of the newly created object
        """
        self.create(
            recipe_id=uuid4(),
            recipe_name=recipe_name,
            creator=creator,
            price=price,
            meal_type=meal_type,
            description=description,
        ).clean()
        return self.last().recipe_id

    def get_recipe_by_id(self, recipe_id: UUID):
        try:
            return self.get(recipe_id=recipe_id)
        except ObjectDoesNotExist:
            return None

    def delete_recipe_by_id(self, recipe_id: UUID) -> bool:
        try:
            recipe_to_delete = self.get(recipe_id=recipe_id)
            recipe_to_delete.delete()
            return True
        except ObjectDoesNotExist:
            return False


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
        name="meal_type", choices=meal_type_options, max_length=2, null=True
    )
    description = models.CharField(name="description", max_length=500, null=True)
    create_date = models.DateTimeField(name="create_date", editable=False, default=now)
    modify_date = models.DateTimeField(name="modify_date", default=now)

    objects = RecipeManager()

    @property
    def id(self) -> UUID:
        return self.recipe_id

    def serialize(self) -> dict:
        return {
            "recipe_id": self.recipe_id,
            "recipe_name": self.recipe_name,
            "creator": self.creator,
            "price": self.price,
            "meal_type": self.get_meal_type_display(),
            "description": self.description,
            "create_date": self.create_date,
            "modify_date": self.modify_date,
        }

    def __str__(self) -> str:
        return f"Recipe({self.recipe_name}, {self.creator}): {self.recipe_id}"
