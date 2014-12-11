from django.core.urlresolvers import reverse
from django.test import Client, TestCase

from users.models import User


class UserRedirectViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass"
        )

    def test_redirect_url(self):
        self.client.login(username="testuser", password="testpass")

        response = self.client.get(reverse('users:redirect'), follow=True)
        self.assertEqual(
            response.redirect_chain,
            [('http://testserver/users/testuser/', 302)]
        )


class UserUpdateViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass"
        )

    def test_get_object(self):
        self.client.login(username="testuser", password="testpass")

        response = self.client.get(reverse('users:update'), follow=True)
        self.assertEqual(
            response.context_data['user'], User.objects.get(
                username='testuser')
        )

    def test_success_url(self):
        self.client.login(username="testuser", password="testpass")

        response = self.client.post(
            reverse('users:update'),
            {'first_name': 'testing'},
            follow=True
        )

        self.assertEqual(
            response.redirect_chain,
            [('http://testserver/users/testuser/', 302)]
        )
