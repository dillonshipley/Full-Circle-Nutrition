import unittest
from django.test import Client

class GetRoutes(unittest.TestCase):
    
    def getIndex(self):
        client = Client()
        res = client.get('/')
        self.assertEquals(res.status_code, 200)