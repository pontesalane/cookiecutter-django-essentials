from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from . import forms
from .models import User


class UserAdmin(AuthUserAdmin):
    form = forms.{{cookiecutter.project_camel_name}}UserChangeForm
    add_form = forms.{{cookiecutter.project_camel_name}}UserCreationForm


admin.site.register(User, UserAdmin)
