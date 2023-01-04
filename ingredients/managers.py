import logging
from uuid import UUID, uuid4

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Manager, Q
from django.db.utils import IntegrityError
from typing import List

log = logging.getLogger("ingredients")


class IngredientManager(Manager):
    def create_ingredient(
        self,
        name: str,
        vegetarian: bool,
        gluten_free: bool,
        calories: float,
        fat: float,
        protein: float,
        units: str,
    ) -> tuple:
        """Creates and validates new ingredient entries to the database. Returns the UUID
        of the new ingredient, or an error if the operation did not complete

        Args:
            name (str): _description_
            vegetarian (bool): _description_
            gluten_free (bool): _description_
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
                gluten_free=gluten_free,
                calories=calories,
                fat=fat,
                protein=protein,
                units=units,
            ).clean()
            return True, self.last().ingredient_id
        except IntegrityError as e:
            return False, e

    def get_ingredient_by_id(self, ingredient_id: UUID) -> tuple:
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

    def get_all_ingredients(self) -> List:
        """Return a list of all ingredients in the database

        Returns:
            List: List of all stored ingredients
        """
        return [ingredient for ingredient in self.all()]

    def get_ingredients_by_filters(
        self,
        name: str = None,
        vegetarian: bool = None,
        gluten_free: bool = None,
        limit: int = None,
        order: str = None,
    ) -> List:
        """Get ingredients from the database using filters provided by the client. 

        Args:
            name (str, optional): _description_. Defaults to None.
            vegetarian (bool, optional): _description_. Defaults to None.
            gluten_free (bool, optional): _description_. Defaults to None.
            limit (int, optional): _description_. Defaults to None.
            order (str, optional): _description_. Defaults to None.

        Returns:
            List: _description_
        """
        ingredient_order = "-"
        ingredient_limit = 10

        ingredient_filters = self.all()

        # Check for the existance of all the filters and apply them to the objects
        if limit is not None:
            ingredient_limit = int(limit)

        # TODO: Fix the ordering implementation
        if order is not None:
            if ingredient_order == "ASC":
                ingredient_order = ingredient_order[:-1]

        if name is not None:
            ingredient_filters = ingredient_filters & self.filter(name=name)

        if vegetarian is not None:
            ingredient_filters = ingredient_filters & self.filter(vegetarian=vegetarian)

        if gluten_free is not None:
            ingredient_filters = ingredient_filters & self.filter(
                gluten_free=gluten_free
            )

        return ingredient_filters.order_by(f"{ingredient_order}modify_date")[:ingredient_limit]

    def delete_ingredients_by_id(self, ingredient_id: UUID) -> bool:
        """Remove an ingedient from the db using the ingredient_id as a query

        Args:
            ingredient_id (UUID): UUID of the ingredient to delete
        Returns:
            bool: Result of the delete operation. True if successful, Fa
        """
        try:
            ingredient_to_delete = self.get(ingredient_id=ingredient_id)
            ingredient_to_delete.delete()
            return True
        except ObjectDoesNotExist:
            return False
