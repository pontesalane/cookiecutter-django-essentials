from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.utils.translation import ugettext_lazy as _

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
    form = forms.UserChangeForm
    add_form = forms.UserCreationForm

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])
