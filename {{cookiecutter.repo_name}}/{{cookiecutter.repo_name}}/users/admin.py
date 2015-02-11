from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

import reversion

from . import forms
from .models import User


@admin.register(User)
class UserAdmin(reversion.VersionAdmin, AuthUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal Information'), {
            'fields': (
                'first_name',
                'last_name',
                'email',
            )
        }),
        (
            _('Permissions'),
            {'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            )}
        ),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    form = forms.{{cookiecutter.project_camel_name}}UserChangeForm
    add_form = forms.{{cookiecutter.project_camel_name}}UserCreationForm
