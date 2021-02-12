from django.test import TestCase, Client
from django.contrib.auth.models import User

class LoginTestClass(TestCase):
    def setUp(self):
        User.objects.create(username='teste.unitario', password='123456')
        self.client = Client()

    def test_login(self):
        response = self.client.post('/login', {
            'username': 'teste.unitario',
            'password': '123456'
        }, **{'Content-Type': 'application/x-www-form-urlencoded'})
        self.assertEqual(response.status_code, 200)