from django.test import TestCase, Client
from accounts.models import User


class RegisterUserTest(TestCase):

    def setUp(self):
        self.profile = User.objects.create_user('test@mail.pl', 'testpwd')

    def test_create_user(self):
        self.assertEqual(self.profile.email, 'test@mail.pl')


class RegisterViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_register(self):
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)
