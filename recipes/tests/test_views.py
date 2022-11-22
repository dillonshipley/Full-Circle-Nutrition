import json
import logging
import time

from recipes.models import Recipe
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

    def test_health_endpoint(self) -> None:
        self.assertTrue(True)

    def test_create_recipe_endpoint(self) -> None:
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

    def test_get_recipe_by_id_endpoint(self) -> None:
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
            RecipeDefaults.RECIPE_GET_SUCCESS_MESSAGE["recipe"],
            get_response_body["recipe"],
        )

        elasped_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elasped_time:.3f} seconds")

    def test_patch_recipe_by_id_endpoint(self) -> None:
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

        # Use the recipe_id of the new recipe to update it in the database
        patch_response = self.client.patch(
            RecipeDefaults.BASE_URL + f"{post_recipe_id}/",
            data=json.dumps(RecipeDefaults.RECIPE_PATCH_REQUEST),
            content_type="application/json",
        )
        patch_response_body = json.loads(patch_response.content)
        patch_recipe_id = patch_response_body["recipe_id"]

        self.assertEqual(patch_recipe_id, post_recipe_id)

        # Retrieve the object again for comparison
        exists, altered_recipe_or_error = Recipe.objects.get_recipe_by_id(
            patch_recipe_id
        )

        self.assertTrue(exists)
        self.assertEqual(patch_response_body["status"], "SUCCESS")
        self.assertEqual(
            RecipeDefaults.RECIPE_PATCH_REQUEST["meal_type"],
            altered_recipe_or_error.meal_type,
        )
        self.assertNotEqual(
            RecipeDefaults.RECIPE_POST_REQUEST["meal_type"],
            altered_recipe_or_error.meal_type,
        )

        elasped_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elasped_time:.3f} seconds")

    def delete_by_id_endpoint(self) -> None:
        start_time = time.perf_counter()

        # Persist the recipe to the DB and assert the success of the operation
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

        # Assert the delete response body matches what's expected
        delete_response = self.client.delete(
            RecipeDefaults.BASE_URL + f"{post_recipe_id}/",
        )
        delete_response_body = json.loads(delete_response.content)
        self.assertEqual(
            delete_response.status_code,
            RecipeDefaults.RECIPE_DELETE_SUCCESS_MESSAGE["status_code"],
        )
        self.assertEqual(
            delete_response_body["status"],
            RecipeDefaults.RECIPE_DELETE_SUCCESS_MESSAGE["status"],
        )
        self.assertEqual(delete_response_body["recipe_id"], post_recipe_id)

        # Assert that the recipe doesn't exist in the db anymore
        result, altered_recipe_or_error = Recipe.objects.get_recipe_by_id(
            post_recipe_id
        )
        self.assertFalse(result)

        elasped_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elasped_time:.3f} seconds")
