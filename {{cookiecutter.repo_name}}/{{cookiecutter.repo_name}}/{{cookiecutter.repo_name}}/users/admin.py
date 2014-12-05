from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from .forms import ZionsUserChangeForm, ZionsUserCreationForm
from .models import User


class UserAdmin(AuthUserAdmin):
    form = ZionsUserChangeForm
    add_form = ZionsUserCreationForm


admin.site.register(User, UserAdmin)
