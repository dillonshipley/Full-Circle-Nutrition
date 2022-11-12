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
        self.assertEqual(
            response.status_code,
            RecipeDefaults.RECIPE_POST_SUCCESS_MESSAGE["status_code"],
        )
        self.assertEqual(
            response_body["status"],
            RecipeDefaults.RECIPE_POST_SUCCESS_MESSAGE["status"],
        )
        log.debug(f"Response body: {response_body}")
        elasped_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elasped_time:.3f} seconds")

    def test_get_recipe_by_id_endpoint(self):
        start_time = time.perf_counter()

        # Persist the user to the DB and assert the success of the operation
        post_response = self.client.post(
            RecipeDefaults.BASE_URL,
            data=json.dumps(RecipeDefaults.RECIPE_POST_REQUEST),
            content_type="application/json",
        )
        post_response_body = json.loads(post_response.content)
        post_recipe_id = post_response_body["recipe_id"]
        self.assertEqual(
            post_response.status_code,
            RecipeDefaults.RECIPE_POST_SUCCESS_MESSAGE["status_code"],
        )

        # Use the recipe_id of the new recipe to retrieve it from the database
        get_response = self.client.get(RecipeDefaults.BASE_URL + f"{post_recipe_id}/")
        get_response_body = json.loads(get_response.content)
        log.debug(f"Response body: {get_response_body}")
        self.assertIsNotNone(get_response_body)
        self.assertEqual(
            get_response.status_code,
            RecipeDefaults.RECIPE_GET_SUCCESS_MESSAGE["status_code"],
        )
        self.assertEqual(
            get_response_body["status"],
            RecipeDefaults.RECIPE_GET_SUCCESS_MESSAGE["status"],
        )
        self.assertIsNotNone(get_response_body["recipe"])
        self.assertEqual(
            get_response_body["recipe"]["recipe_id"], post_response_body["recipe_id"]
        )
        self.assertDictContainsSubset(
            get_response_body['recipe'], RecipeDefaults.RECIPE_GET_SUCCESS_MESSAGE['recipe']
        )

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
