from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from petstagram_last.accounts.forms import RegisterForm

UserModel=get_user_model()

@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    list_display = ('username', 'email',)
    ordering = ('first_name',)
    add_form = RegisterForm
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'username',
                    'password',
                ),
            }),
        (
            'Personal info',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'gender'
                ),
            },
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (
            'Important dates',
            {
                'fields': (
                    'last_login',
                    'date_joined',
                ),
            },
        ),
    )