import logging
import time

from django.core.exceptions import ValidationError
from django.test import TestCase

from users.models import User

log = logging.getLogger("test")


class UserTests(TestCase):
    USER_DEFAULTS = {
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

    def test_create_valid_user_with_only_required_fields(self) -> None:
        start_time = time.perf_counter()
        elapsed_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elapsed_time:.3f} seconds")

    def test_create_valid_user_object_with_all_defaults(self) -> None:
        start_time = time.perf_counter()

        new_user = User(
            user_id=self.USER_DEFAULTS["default_valid_user"]["user_id"],
            user_name=self.USER_DEFAULTS["default_valid_user"]["user_name"],
            age=self.USER_DEFAULTS["default_valid_user"]["age"],
            height=self.USER_DEFAULTS["default_valid_user"]["height"],
            weight=self.USER_DEFAULTS["default_valid_user"]["weight"],
            body_fat=self.USER_DEFAULTS["default_valid_user"]["body_fat"],
            goal=self.USER_DEFAULTS["default_valid_user"]["goal"],
        )

        self.assertEqual(
            new_user.user_id, self.USER_DEFAULTS["default_valid_user"]["user_id"]
        )
        self.assertEqual(
            new_user.user_name, self.USER_DEFAULTS["default_valid_user"]["user_name"]
        )
        self.assertEqual(new_user.age, self.USER_DEFAULTS["default_valid_user"]["age"])
        self.assertEqual(
            new_user.height, self.USER_DEFAULTS["default_valid_user"]["height"]
        )
        self.assertEqual(
            new_user.weight, self.USER_DEFAULTS["default_valid_user"]["weight"]
        )
        self.assertEqual(
            new_user.body_fat, self.USER_DEFAULTS["default_valid_user"]["body_fat"]
        )
        self.assertEqual(
            new_user.goal, self.USER_DEFAULTS["default_valid_user"]["goal"]
        )

        new_user.clean()

        elapsed_time = time.perf_counter() - start_time
        log.info(f"{new_user}")
        log.info(f"[+] Completed in {elapsed_time:.3f} seconds")

    def test_create_user_with_invalid_user_id(self) -> None:
        start_time = time.perf_counter()

        invalid_user = User(
            user_id=self.USER_DEFAULTS["invalid_user_id"]["user_id"],
            user_name="invalid_user",
            age=self.USER_DEFAULTS["default_valid_user"]["age"],
            height=self.USER_DEFAULTS["default_valid_user"]["height"],
            weight=self.USER_DEFAULTS["default_valid_user"]["weight"],
            body_fat=self.USER_DEFAULTS["default_valid_user"]["body_fat"],
            goal=self.USER_DEFAULTS["default_valid_user"]["goal"],
        )

        with self.assertRaises(ValidationError):
            invalid_user.save()

        elapsed_time = time.perf_counter() - start_time
        log.info(msg=f"{invalid_user}")
        log.info(f"[+] Completed in {elapsed_time:.3f} seconds")
