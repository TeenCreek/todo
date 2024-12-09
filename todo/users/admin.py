from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MyUser


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
    )
    ordering = ('id', 'username')

    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {'fields': ('age', 'bio')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Дополнительная информация', {'fields': ('age', 'bio')}),
    )
