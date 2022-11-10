import logging
import time

from django.core.exceptions import ValidationError
from django.test import TestCase

from recipes.models import Recipe
from recipes.tests.defaults import RecipeDefaults

log = logging.getLogger("test")


class RecipeTests(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_create_valid_recipe_object_with_all_defaults(self) -> None:
        start_time = time.perf_counter()

        new_recipe = Recipe(
            recipe_id=RecipeDefaults.RECIPE_ID,
            recipe_name=RecipeDefaults.RECIPE_NAME,
            creator=RecipeDefaults.CREATOR,
            price=RecipeDefaults.PRICE,
            meal_type=RecipeDefaults.MEAL_TYPE,
            description=RecipeDefaults.DESCRIPTION
        )
        
        self.assertEqual(new_recipe.recipe_id, RecipeDefaults.RECIPE_ID)
        self.assertEqual(new_recipe.recipe_name, RecipeDefaults.RECIPE_NAME)
        self.assertEqual(new_recipe.creator, RecipeDefaults.CREATOR)
        self.assertEqual(new_recipe.price, RecipeDefaults.PRICE)
        self.assertEqual(new_recipe.meal_type, RecipeDefaults.MEAL_TYPE)
        self.assertEqual(new_recipe.description, RecipeDefaults.DESCRIPTION)
        self.assertIsNotNone(new_recipe.create_date)
        self.assertIsNotNone(new_recipe.modify_date)

        new_recipe.clean()
        new_recipe.save()

        elapsed_time = time.perf_counter() - start_time
        log.info(f"{new_recipe}")
        log.info(f"[+] Completed in {elapsed_time:.3f} seconds")