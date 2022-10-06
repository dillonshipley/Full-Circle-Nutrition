import logging
import time

from django.core.exceptions import ValidationError
from django.test import TestCase

from recipes.models import User

log = logging.getLogger("test")


class RecipeTests(TestCase):
    def setUp(self) -> None:
        return super().setUp()


class UserTests(TestCase):
    user_defaults = {
        "default_valid_user": {
            "user_id": "10000000-0000-0000-0000-000000000000",
            "user_name": "user",
            "age": 1,
            "height": 64.5,
            "weight": 64.5,
            "body_fat": 0.05,
            "goal": "0",
        },
        "invalid_user_id": {
            "user_id": "1",
        },
    }

    def setUp(self) -> None:
        return super().setUp()

    def test_create_valid_user_object(self) -> None:
        start_time = time.perf_counter()
        log.info(f"Started test_create_valid_user_object at {start_time:.3f}")

        new_user = User(
            user_id=self.user_defaults["default_valid_user"]["user_id"],
            user_name=self.user_defaults["default_valid_user"]["user_name"],
            age=self.user_defaults["default_valid_user"]["age"],
            height=self.user_defaults["default_valid_user"]["height"],
            weight=self.user_defaults["default_valid_user"]["weight"],
            body_fat=self.user_defaults["default_valid_user"]["body_fat"],
            goal=self.user_defaults["default_valid_user"]["goal"],
        )

        self.assertEqual(
            new_user.user_id, self.user_defaults["default_valid_user"]["user_id"]
        )
        self.assertEqual(
            new_user.user_name, self.user_defaults["default_valid_user"]["user_name"]
        )
        self.assertEqual(new_user.age, self.user_defaults["default_valid_user"]["age"])
        self.assertEqual(
            new_user.height, self.user_defaults["default_valid_user"]["height"]
        )
        self.assertEqual(
            new_user.weight, self.user_defaults["default_valid_user"]["weight"]
        )
        self.assertEqual(
            new_user.body_fat, self.user_defaults["default_valid_user"]["body_fat"]
        )
        self.assertEqual(
            new_user.goal, self.user_defaults["default_valid_user"]["goal"]
        )

        elapsed_time = time.perf_counter() - start_time
        log.info(f"{new_user}")
        log.info(f"Completed test_create_valid_user_object in {elapsed_time:.3f}")

    def test_create_user_with_invalid_user_id(self) -> None:
        start_time = time.perf_counter()
        log.info(f"Started test_create_user_with_invalid_user_id at {start_time:.3f}")

        invalid_user = User(
            user_id=self.user_defaults["invalid_user_id"]["user_id"],
            user_name="invalid_user",
            age=self.user_defaults["default_valid_user"]["age"],
            height=self.user_defaults["default_valid_user"]["height"],
            weight=self.user_defaults["default_valid_user"]["weight"],
            body_fat=self.user_defaults["default_valid_user"]["body_fat"],
            goal=self.user_defaults["default_valid_user"]["goal"],
        )

        with self.assertRaises(ValidationError):
            invalid_user.save()

        elapsed_time = time.perf_counter() - start_time
        log.info(f"{invalid_user}")
        log.info(
            f"Completed test_create_user_with_invalid_user_id in {elapsed_time:.3f}"
        )
