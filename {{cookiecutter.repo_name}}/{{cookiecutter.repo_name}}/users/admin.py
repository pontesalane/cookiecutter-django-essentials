from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from .forms import {{cookiecutter.project_camel_name}}UserChangeForm, {{cookiecutter.project_camel_name}}UserCreationForm
from .models import User


class UserAdmin(AuthUserAdmin):
    form = {{cookiecutter.project_camel_name}}UserChangeForm
    add_form = {{cookiecutter.project_camel_name}}UserCreationForm


admin.site.register(User, UserAdmin)
