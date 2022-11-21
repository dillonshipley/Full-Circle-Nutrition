import logging
import time

from django.test import TestCase

log = logging.getLogger("test")


class RecipeTests(TestCase):
    def setUp(self) -> None:
        return super().setUp()
