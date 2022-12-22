from uuid import UUID, uuid4

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.utils import IntegrityError

from typing import List, Tuple


class RecipeManager(models.Manager):
    def create_recipe(
        self,
        recipe_name: str,
        creator: str,
        price: float,
        meal_type: str,
        description: str,
    ) -> tuple:
        """Creates and validates new recipe entries to the database. Returns the UUID of the
        new recipe

        Args:
            recipe_name (str): Name of the recipe that should be created
            creator (str): Creator of the new recipe
            price (float): Total price of the recipe
            meal_type (str): Meal type enum value
            description (str): Description of the new meal
        Returns:
            tuple: Result of the operation and the UUID of the new recipe, or an error message
        """
        try:
            self.create(
                recipe_id=uuid4(),
                recipe_name=recipe_name,
                creator=creator,
                price=price,
                meal_type=meal_type,
                description=description,
            ).clean()
            return True, self.last().recipe_id
        except IntegrityError as e:
            return False, e

    def get_recipes(self, amount: int = -1) -> Tuple:
        recipes = list()

        if amount == -1:
            recipes = [recipe for recipe in self.all()]

        return True, recipes

    def get_recipe_by_id(self, recipe_id: UUID) -> tuple:
        """Retrieve a recipe using the recipe_id as a query

        Args:
            recipe_id (UUID): Recipe id of the Recipe model that should be restored
        Returns:
            tuple(bool, [Recipe | Error]): Tuple containing the success of the operation,
            and the resulting recipe or error
        """
        try:
            return True, self.get(recipe_id=recipe_id)
        except ObjectDoesNotExist as e:
            return False, e

    def delete_recipe_by_id(self, recipe_id: UUID) -> bool:
        """Remove a recipe from the db using the recipe_id as a query

        Args:
            recipe_id (UUID): UUID of the recipe that should be delete
        Returns:
            bool: True if the object was successfully removed from the db, False otherwise
        """
        try:
            recipe_to_delete = self.get(recipe_id=recipe_id)
            recipe_to_delete.delete()
            return True
        except ObjectDoesNotExist:
            return False
