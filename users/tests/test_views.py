import logging
import time

from django.test import RequestFactory, TestCase
from django.test import Client
from django.utils import timezone
from users.models import User

log = logging.getLogger("test")


class UserViewTests(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.client = Client()
        return super().setUp()

    def test_create_user_method(self):
        response = self.client.post('')

    def test_get_by_id(self):  
        response = self.client.get(f"/v1/users/{}")

    def test_patch_by_id(self):
        pass    

    def test_delete_by_id(self):
        pass