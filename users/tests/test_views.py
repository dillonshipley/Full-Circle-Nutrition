import logging
import time

from django.test import RequestFactory, TestCase

from users.views import create_user, user_interactions_by_id
from users.models import User

class UserViewTests(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        return super().setUp()

    def test_create_user_method(self):
        pass

    def test_get_by_id(self):
        pass

    def test_patch_by_id(self):
        pass    

    def test_delete_by_id(self):
        pass