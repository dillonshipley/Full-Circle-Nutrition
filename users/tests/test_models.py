import logging
import time

from django.core.exceptions import ValidationError
from django.test import TestCase

from .defaults import UserDefaults
from users.models import User

log = logging.getLogger("test")


class UserTests(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_create_valid_user_object_with_all_defaults(self) -> None:
        start_time = time.perf_counter()

        new_user = User(
            user_id=UserDefaults.USER_ID,
            user_name=UserDefaults.USER_NAME,
            age=UserDefaults.AGE,
            height=UserDefaults.HEIGHT,
            weight=UserDefaults.WEIGHT,
            body_fat=UserDefaults.BODY_FAT,
            goal=UserDefaults.GOAL,
        )

        self.assertEqual(new_user.user_id, UserDefaults.USER_ID)
        self.assertEqual(new_user.user_name, UserDefaults.USER_NAME)
        self.assertEqual(new_user.age, UserDefaults.AGE)
        self.assertEqual(new_user.height, UserDefaults.HEIGHT)
        self.assertEqual(new_user.weight, UserDefaults.WEIGHT)
        self.assertEqual(new_user.body_fat, UserDefaults.BODY_FAT)
        self.assertEqual(new_user.goal, UserDefaults.GOAL)

        new_user.clean()
        new_user.save()

        elapsed_time = time.perf_counter() - start_time
        log.info(f"{new_user}")
        log.info(f"[+] Completed in {elapsed_time:.3f} seconds")
