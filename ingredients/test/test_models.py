import logging
import time

from django.core.exceptions import ValidationError
from django.test import TestCase

from .defaults import IngredientDefaults
from ingredients.models import Ingredient

log  = logging.getLogger("test")


class IngredientTests(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_create_valid_ingredient_with_all_defaults(self) -> None:
        start_time = time.perf_counter()

        new_ingredient = Ingredient(
            ingredient_id=IngredientDefaults
        )

        new_ingredient.clean()
        new_ingredient.save()

        elasped_time = time.perf_counter() - start_time
        log.info(f"{new_ingredient}")
        log.info(f"[+] Completed in {elasped_time:.3f} seconds")