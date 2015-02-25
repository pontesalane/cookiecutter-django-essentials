from django.test import TestCase

from users.forms import UserCreationForm
from users.models import User


class UserCreationTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create(
            username='testuser',
            email='test@test.com',
            password='password'
        )

        self.bad_form = UserCreationForm({
            'username': 'testuser',
            'password1': 'password',
            'password2': 'password',
        })

        self.good_form = UserCreationForm({
            'username': 'testuser2',
            'password1': 'password',
            'password2': 'password',
        })

    def test_username_good(self):
        self.assertTrue(self.good_form.is_valid())

    def test_clean_username_bad(self):
        self.assertFalse(self.bad_form.is_valid())
