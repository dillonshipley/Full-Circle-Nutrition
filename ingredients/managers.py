from uuid import UUID, uuid4

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Manager
from django.db.utils import IntegrityError

from .models import Ingredient


class IngredientManager(Manager):
    def create_ingredient(
        self,
        name: str,
        vegetarian: bool,
        calories: float,
        fat: float,
        protein: float,
        units: str,
    ) -> tuple[bool, (UUID | IntegrityError)]:
        """Creates and validates new ingredient entries to the database. Returns the UUID 
        of the new ingredient, or an error if the operation did not complete

        Args:
            name (str): _description_
            vegetarian (bool): _description_
            calories (float): _description_
            fat (float): _description_
            protein (float): _description_
            units (str): _description_
        Returns:
            tuple: _description_
        """
        try:
            self.create(
                ingredient_id=uuid4(),
                name=name,
                vegetarian=vegetarian,
                calories=calories,
                fat=fat,
                protein=protein,
                units=units,
            ).clean()
            return True, self.last().ingredient_id
        except IntegrityError as e:
            return False, e

    def get_ingredient_by_id(
        self, ingredient_id: UUID
    ) -> tuple[bool, (Ingredient | ObjectDoesNotExist)]:
        """Retrieve an ingredient from the database using the ingredient_id as the query

        Args:
            ingredient_id (UUID): UUID of the ingredient model that should be restored
        Returns:
            tuple: _description_
        """
        try:
            return True, self.get(ingredient_id=ingredient_id)
        except ObjectDoesNotExist as e:
            return False, e

    def delete_ingredients_by_id(self, ingredient_id: UUID) -> bool:
        """Remove an ingedient from the db using the ingredient_id as a query

        Args:
            ingredient_id (UUID): _description_
        Returns:
            bool: _description_
        """
        try:
            ingredient_to_delete = self.get(ingredient_id=ingredient_id)
            ingredient_to_delete.delete()
            return True
        except ObjectDoesNotExist:
            return False
