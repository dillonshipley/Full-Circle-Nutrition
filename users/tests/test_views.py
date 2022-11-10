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
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response_body['status'], UserDefaults.USER_POST_SUCCESS_MESSAGE["status"]
        )
        log.debug(f"Response body: {response_body}")
        elapsed_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elapsed_time:.5f} seconds")

    def test_get_by_id_endpoint(self):
        start_time = time.perf_counter()
        response = self.client.get(UserDefaults.BASE_URL + f"{UserDefaults.USER_ID}")
        elapsed_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elapsed_time:.5f} seconds")

    def test_patch_by_id_endpoint(self):
        pass

    def test_delete_by_id_endpoint(self):
        pass
