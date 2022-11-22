import json
import logging
import re
import time
from uuid import uuid4

from django.test import Client, RequestFactory, TestCase

from users.models import User
from users.tests.defaults import UserDefaults

log = logging.getLogger("test")


class UserViewTests(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.client = Client()
        return super().setUp()

    def test_create_user_endpoint(self):
        start_time = time.perf_counter()
        response = self.client.post(
            UserDefaults.BASE_URL,
            data=json.dumps(UserDefaults.USER_POST_REQUEST),
            content_type="application/json",
        )
        response_body = json.loads(response.content)
        self.assertEqual(
            response.status_code,
            UserDefaults.USER_POST_SUCCESS_MESSAGE["status_code"],
        )
        self.assertEqual(
            response_body["status"], UserDefaults.USER_POST_SUCCESS_MESSAGE["status"]
        )
        log.debug(f"Response body: {response_body}")
        elapsed_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elapsed_time:.5f} seconds")

    def test_get_by_id_endpoint(self):
        start_time = time.perf_counter()

        # Persist the user to the DB and assert the success of the operation
        post_response = self.client.post(
            UserDefaults.BASE_URL,
            data=json.dumps(UserDefaults.USER_POST_REQUEST),
            content_type="application/json",
        )
        post_response_body = json.loads(post_response.content)
        post_user_id = post_response_body["user_id"]
        self.assertEqual(
            post_response.status_code,
            UserDefaults.USER_POST_SUCCESS_MESSAGE["status_code"],
        )

        # Use the user_id of the new user to retrieve from the DB
        get_response = self.client.get(UserDefaults.BASE_URL + f"{post_user_id}/")
        get_response_body = json.loads(get_response.content)
        log.debug(f"Response body: {get_response_body}")
        self.assertIsNotNone(get_response_body)
        self.assertAlmostEqual(
            get_response.status_code,
            UserDefaults.USER_GET_SUCCESS_MESSAGE["status_code"],
        )
        self.assertAlmostEqual(
            get_response_body["status"], UserDefaults.USER_GET_SUCCESS_MESSAGE["status"]
        )
        self.assertIsNotNone(get_response_body["user"])
        self.assertEqual(
            get_response_body["user"]["user_id"], post_response_body["user_id"]
        )
        self.assertDictContainsSubset(
            UserDefaults.USER_GET_SUCCESS_MESSAGE["user"], get_response_body["user"]
        )

        elapsed_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elapsed_time:.5f} seconds")

    def test_patch_by_id_endpoint(self):
        start_time = time.perf_counter()

        # Persist user to the DB and assert the success of the operation
        post_response = self.client.post(
            UserDefaults.BASE_URL,
            data=json.dumps(UserDefaults.USER_POST_REQUEST),
            content_type="application/json",
        )
        post_response_body = json.loads(post_response.content)
        post_user_id = post_response_body["user_id"]
        self.assertEqual(
            post_response.status_code,
            UserDefaults.USER_POST_SUCCESS_MESSAGE["status_code"],
        )

        # Use the user_id of the new user to update it in the database
        patch_response = self.client.patch(
            UserDefaults.BASE_URL + f"{post_user_id}/",
            data=json.dumps(UserDefaults.USER_PATCH_REQUEST),
            content_type="application/json",
        )
        patch_response_body = json.loads(patch_response.content)
        patch_user_id = patch_response_body["user_id"]

        self.assertEqual(post_user_id, patch_user_id)

        # Retrieve the object again for comparison
        exists, altered_user_or_error = User.objects.get_user_by_id(patch_user_id)

        self.assertTrue(exists)
        self.assertEqual(patch_response_body["status"], "SUCCESS")
        self.assertEqual(
            UserDefaults.USER_PATCH_REQUEST["goal"], altered_user_or_error.goal
        )
        self.assertNotEqual(
            UserDefaults.USER_POST_REQUEST["goal"], altered_user_or_error.goal
        )

        elapsed_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elapsed_time:.5f} seconds")

    def test_delete_by_id_endpoint(self):
        start_time = time.perf_counter()

        # Persist the user to the database and assert the success of the operation
        post_response = self.client.post(
            UserDefaults.BASE_URL,
            data=json.dumps(UserDefaults.USER_POST_REQUEST),
            content_type="application/json",
        )
        post_response_body = json.loads(post_response.content)
        post_user_id = post_response_body["user_id"]
        self.assertEqual(
            post_response.status_code,
            UserDefaults.USER_POST_SUCCESS_MESSAGE["status_code"],
        )

        # Assert the delete response body matches what's expected 
        delete_response = self.client.delete(
            UserDefaults.BASE_URL + f"{post_user_id}/",
        )
        delete_response_body = json.loads(delete_response.content)
        self.assertEqual(
            delete_response.status_code,
            UserDefaults.USER_DELETE_SUCCESS_MESSAGE["status_code"],
        )
        self.assertEqual(
            delete_response_body["status"],
            UserDefaults.USER_DELETE_SUCCESS_MESSAGE["status"],
        )
        self.assertEqual(delete_response_body["user_id"], post_user_id)

        # Assert that the recipe doesn't exist in the db anymore
        exists, altered_user_or_error = User.objects.get_user_by_id(post_user_id)
        self.assertFalse(exists)

        elapsed_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elapsed_time:.5f} seconds")
