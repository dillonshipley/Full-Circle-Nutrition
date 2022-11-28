import logging
import time

from django.core.exceptions import ValidationError
from django.test import TestCase

from .defaults import IngredientDefaults
from ingredients.models import Ingredient

log = logging.getLogger("test")


class IngredientTests(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_create_valid_ingredient_with_all_defaults(self) -> None:
        start_time = time.perf_counter()

        new_ingredient = Ingredient(
            ingredient_id=IngredientDefaults.INGREDIENT_ID,
            name=IngredientDefaults.NAME,
            vegetarian=IngredientDefaults.VEGETARIAN,
            calories=IngredientDefaults.CALORIES,
            fat=IngredientDefaults.FAT,
            protein=IngredientDefaults.PROTEIN,
            units=IngredientDefaults.UNITS,
        )

        self.assertEqual(new_ingredient.ingredient_id, IngredientDefaults.INGREDIENT_ID)
        self.assertEqual(new_ingredient.name, IngredientDefaults.NAME)
        self.assertEqual(new_ingredient.vegetarian, IngredientDefaults.VEGETARIAN)
        self.assertEqual(new_ingredient.calories, IngredientDefaults.CALORIES)
        self.assertEqual(new_ingredient.fat, IngredientDefaults.FAT)
        self.assertEqual(new_ingredient.protein, IngredientDefaults.PROTEIN)
        self.assertEqual(new_ingredient.units, IngredientDefaults.UNITS)

        new_ingredient.clean()
        new_ingredient.save()

        elasped_time = time.perf_counter() - start_time
        log.info(f"{new_ingredient}")
        log.info(f"[+] Completed in {elasped_time:.3f} seconds")
