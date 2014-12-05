from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class UserForm(forms.ModelForm):

    class Meta:
        # Set this form to use the User model.
        model = User

        # Constrain the UserForm to just these fields.
        fields = ("first_name", "last_name")


class {{cookiecutter.project_camel_name}}UserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = User


class {{cookiecutter.project_camel_name}}UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
