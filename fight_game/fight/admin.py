from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import FightUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = FightUser
    list_display = [
        "email",
        "username",
    ]


admin.site.register(FightUser, CustomUserAdmin)
