from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

import reversion

from . import forms
from .models import User


class UserAdmin(reversion.VersionAdmin, AuthUserAdmin):
    form = forms.{{cookiecutter.project_camel_name}}UserChangeForm
    add_form = forms.{{cookiecutter.project_camel_name}}UserCreationForm


admin.site.register(User, UserAdmin)
