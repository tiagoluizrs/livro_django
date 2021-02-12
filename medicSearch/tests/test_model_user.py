from django.test import TestCase
from django.contrib.auth.models import User

class UserModelTestClass(TestCase):
    def setUp(self):
        User.objects.create(username='teste.unitario', password='123456')

    def test_user_exist(self):
        user = User.objects.first()
        self.assertIsNotNone(user)