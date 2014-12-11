from django.test import TestCase

from users.models import User


class UserTestCase(TestCase):

    def setUp(self):
        User.objects.create(
            username='testuser', email='test@test.com', password='password')

    def test_user_str_value(self):
        test_user = User.objects.get(username='testuser')
        self.assertEqual(test_user.__str__(), "testuser")
