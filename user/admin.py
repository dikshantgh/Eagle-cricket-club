from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import Player


@admin.register(Player)
class PlayerAdmin(UserAdmin):
    add_fieldsets = (
        (
            'Signup',
            {
                "fields": ('username', 'email', 'password1', 'password2'),
            },
        ),
    )
    list_display = ['username', 'email', ]