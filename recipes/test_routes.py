from imghdr import tests
from django.test import TestCase, Client

class GetRoutes(TestCase):
    
    def getIndex(self):
        client = Client()
        res = client.get('/')
        self.assertEquals(res.status_code, 200)