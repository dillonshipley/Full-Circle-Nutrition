import json
import time
import logging

from django.test import TestCase
from .defaults import IngredientDefaults

log = logging.getLogger('test')


class GetIngredientByFiltersValidatorTests(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_should_return_false_when_no_filters_provided():
        pass