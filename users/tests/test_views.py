import logging
import re
import time
import json
from uuid import uuid4

from django.test import RequestFactory, TestCase
from django.test import Client
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
            UserDefaults.USER_POST_SUCCESS_MESSAGE["status_message"],
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
        elapsed_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elapsed_time:.5f} seconds")

    def test_delete_by_id_endpoint(self):
        start_time = time.perf_counter()
        elapsed_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elapsed_time:.5f} seconds")
