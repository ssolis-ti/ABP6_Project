from django.test import TestCase
from django.urls import reverse

class UsersTestCase(TestCase):
    def test_signup_view_status_code(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_status_code(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
