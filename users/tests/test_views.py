import logging
import time

from django.test import RequestFactory, TestCase
from django.test import Client
from defaults import UserDefaults

log = logging.getLogger("test")


class UserViewTests(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.client = Client()
        return super().setUp()

    def test_create_user_method(self):
        start_time = time.perf_counter()
        response = self.client.post('', data=UserDefaults.USER_POST_REQUEST)

        elapsed_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elapsed_time:.5f} seconds")

    def test_get_by_id(self):  
        start_time = time.perf_counter()
        response = self.client.get(f"/v1/users/")
        elapsed_time = time.perf_counter() - start_time
        log.info(f"[+] Completed in {elapsed_time:.5f} seconds")

    def test_patch_by_id(self):
        pass    

    def test_delete_by_id(self):
        pass