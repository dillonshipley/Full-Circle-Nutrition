import json
import logging
import time
from unittest import TestCase
from uuid import uuid4

from django.test import Client, RequestFactory, TestCase

from recipes.tests.defaults import RecipeDefaults

log = logging.getLogger("test")


class TestInformationRoutes(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.client = Client()
        return super().setUp()

    def test_health_endpoint(self):
        self.assertTrue(True)

    def test_create_recipe_endpoint(self):
        start_time = time.perf_counter()
        response = self.client.post(
            RecipeDefaults.BASE_URL,
            data=json.dumps(RecipeDefaults.RECIPE_POST_REQUEST),
            content_type="application/json",
        )
        response_body = json.loads(response.content)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response_body["status"],
            RecipeDefaults.RECIPE_POST_SUCCESS_MESSAGE["status"],
        )
        log.debug(f"Response body: {response_body}")
        elasped_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elasped_time:.3f} seconds")

    def test_get_recipe_by_id_endpoint(self):
        start_time = time.perf_counter()

        elasped_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elasped_time:.3f} seconds")

    def test_patch_recipe_by_id_endpoint(self):
        start_time = time.perf_counter()

        elasped_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elasped_time:.3f} seconds")

    def delete_by_id_endpoint(self):
        start_time = time.perf_counter()

        elasped_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elasped_time:.3f} seconds")
