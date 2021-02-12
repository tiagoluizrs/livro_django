from django.test import TestCase, Client
from django.contrib.auth.models import User
from medicSearch.models.Profile import Profile
from django.db import transaction, IntegrityError

class MedicViewTestClass(TestCase):
    def setUp(self):
        try:
            with transaction.atomic():
                user = User.objects.create(username='teste.unitario', password='123456')
                profile = Profile.objects.get(user=user)
                profile.role = 2
                profile.save()
        except IntegrityError as e:
            print("Erro ao criar usuário. Descrição: %s" % e)

        self.client = Client()

    def test_medics_list(self):
        response = self.client.get('/medic/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Foram encontrados: 1 medico(s)')