import json
import logging
import time

from django.test import Client, RequestFactory, TestCase
from django.core.exceptions import ObjectDoesNotExist

from ingredients.models import Ingredient
from .defaults import IngredientDefaults

log = logging.getLogger("test")


class IngredientsViewTests(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.client = Client()
        return super().setUp()

    def test_create_ingredient_endpoint(self) -> None:
        start_time = time.perf_counter()

        response = self.client.post(
            IngredientDefaults.BASE_URL,
            data=json.dumps(IngredientDefaults.INGREDIENT_POST_REQUEST),
            content_type="application/json",
        )

        response_body = json.loads(response.content)
        self.assertIsNotNone(response_body)
        self.assertEqual(
            response.status_code,
            IngredientDefaults.INGREDIENT_POST_SUCCESS_MESSAGE["status_code"],
        )
        self.assertEqual(
            response_body["status"],
            IngredientDefaults.INGREDIENT_POST_SUCCESS_MESSAGE["status"],
        )

        log.debug(f"Response body: {response_body}")
        elapsed_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elapsed_time:.5f} seconds")

    def test_get_by_id_endpoint(self) -> None:
        start_time = time.perf_counter()

        # Persist the ingredient to the DB and assert the success of the operation
        post_response = self.client.post(
            IngredientDefaults.BASE_URL,
            data=json.dumps(IngredientDefaults.INGREDIENT_POST_REQUEST),
            content_type="application/json",
        )
        post_response_body = json.loads(post_response.content)
        post_ingredient_id = post_response_body["ingredient_id"]
        self.assertEqual(
            post_response.status_code,
            IngredientDefaults.INGREDIENT_POST_SUCCESS_MESSAGE["status_code"],
        )

        # Use the ingredient_id of the new user to retrieve from the DB
        get_response = self.client.get(
            IngredientDefaults.BASE_URL + f"{post_ingredient_id}/"
        )
        get_response_body = json.loads(get_response.content)
        log.debug(f"Response body: {get_response_body}")
        self.assertIsNotNone(get_response_body)
        self.assertIsNotNone(get_response_body["ingredient"])
        self.assertAlmostEqual(
            get_response.status_code,
            IngredientDefaults.INGREDIENT_GET_SUCCESS_MESSAGE["status_code"],
        )
        self.assertEqual(
            get_response.status_code,
            IngredientDefaults.INGREDIENT_GET_SUCCESS_MESSAGE["status_code"],
        )
        self.assertEqual(
            get_response_body["ingredient"]["ingredient_id"],
            post_response_body["ingredient_id"],
        )
        self.assertDictContainsSubset(
            IngredientDefaults.INGREDIENT_GET_SUCCESS_MESSAGE["ingredient"],
            get_response_body["ingredient"],
        )

        elapsed_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elapsed_time:.5f} seconds")

    def test_patch_by_id_endpoint(self) -> None:
        start_time = time.perf_counter()

        # Persist the ingredient to the DB and assert the success of the operation
        post_response = self.client.post(
            IngredientDefaults.BASE_URL,
            data=json.dumps(IngredientDefaults.INGREDIENT_POST_REQUEST),
            content_type="application/json",
        )
        post_response_body = json.loads(post_response.content)
        post_ingredient_id = post_response_body["ingredient_id"]
        self.assertEqual(
            post_response.status_code,
            IngredientDefaults.INGREDIENT_POST_SUCCESS_MESSAGE["status_code"],
        )

        # Use the ingredient_id of the new ingredient to update it in the database
        patch_response = self.client.patch(
            IngredientDefaults.BASE_URL + f"{post_ingredient_id}/",
            data=json.dumps(IngredientDefaults.INGREDIENT_PATCH_REQUEST),
            content_type="application/json",
        )
        patch_response_body = json.loads(patch_response.content)
        patch_ingredient_id = patch_response_body["ingredient_id"]

        self.assertEqual(patch_ingredient_id, post_ingredient_id)

        # Retrieve the object again for comparison
        exists, altered_ingredient_or_error = Ingredient.objects.get_ingredient_by_id(
            patch_ingredient_id
        )
        self.assertTrue(exists)
        self.assertEqual(patch_response_body["status"], "SUCCESS")
        self.assertEqual(
            IngredientDefaults.INGREDIENT_PATCH_REQUEST["fat"],
            altered_ingredient_or_error.fat,
        )
        self.assertNotEqual(
            IngredientDefaults.INGREDIENT_POST_REQUEST["fat"],
            altered_ingredient_or_error.fat,
        )

        elapsed_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elapsed_time:.5f} seconds")

    def test_delete_by_id_endpoint(self) -> None:
        start_time = time.perf_counter()

        # Persist the ingredient to the DB and assert the success of the operation
        post_response = self.client.post(
            IngredientDefaults.BASE_URL,
            data=json.dumps(IngredientDefaults.INGREDIENT_POST_REQUEST),
            content_type="application/json",
        )
        post_response_body = json.loads(post_response.content)
        post_ingredient_id = post_response_body["ingredient_id"]
        self.assertEqual(
            post_response.status_code,
            IngredientDefaults.INGREDIENT_POST_SUCCESS_MESSAGE["status_code"],
        )

        # Assert the delete response body matches what is expected
        delete_response = self.client.delete(
            IngredientDefaults.BASE_URL + f"{post_ingredient_id}/"
        )
        delete_response_body = json.loads(delete_response.content)
        self.assertEqual(
            IngredientDefaults.INGREDIENT_DELETE_SUCCESS_MESSAGE["status_code"],
            delete_response.status_code,
        )
        self.assertEqual(
            IngredientDefaults.INGREDIENT_DELETE_SUCCESS_MESSAGE["status"],
            delete_response_body["status"],
        )
        self.assertEqual(delete_response_body["ingredient_id"], post_ingredient_id)

        # Assert the ingredient doesn't exist in the database anymore
        result, altered_recipe_or_error = Ingredient.objects.get_ingredient_by_id(
            post_ingredient_id
        )
        self.assertFalse(result)

        elapsed_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elapsed_time:.5f} seconds")
