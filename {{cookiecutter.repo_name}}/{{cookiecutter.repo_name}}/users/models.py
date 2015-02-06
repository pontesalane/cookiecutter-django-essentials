# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser


# Subclass AbstractUser
class User(AbstractUser):

    def __str__(self):
        return self.username
