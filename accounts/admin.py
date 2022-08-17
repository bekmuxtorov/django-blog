from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForms
from .models import CustomUser


# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForms
    model = CustomUser

    list_display = ['email', 'username', 'first_name', 'last_name', 'region', 'is_staff']

    fieldsets = (
        (None, {
            "fields": (
               'email', 'region', 'first_name', 'last_name'
            ),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ( 'first_name', 'last_name','email', 'region',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)

"""
Tajriba_1 : list_desplay nima ekanligini bilamiz
    Natija_1: Admin panelda ko'rinadigon xossa nomlari

Tajriba_2 : fieldsets nima ekanligi bilmoqchimiz
    Natija_2: Admin paneldan o'zgartirish mumkin bo'lgan qiymatlar saqlanadi
"""
