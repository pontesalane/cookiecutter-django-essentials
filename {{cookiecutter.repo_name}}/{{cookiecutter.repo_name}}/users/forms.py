from django import forms
from django.contrib.auth.forms import (
    UserChangeForm as DjangoUserChangeForm,
    UserCreationForm as DjangoUserCreationForm
)

from .models import User


class UserForm(forms.ModelForm):

    class Meta:
        # Set this form to use the User model.
        model = User

        # Constrain the UserForm to just these fields.
        fields = ("first_name", "last_name")


class UserChangeForm(DjangoUserChangeForm):

    class Meta(DjangoUserChangeForm.Meta):
        model = User


class UserCreationForm(DjangoUserCreationForm):

    class Meta(DjangoUserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])
