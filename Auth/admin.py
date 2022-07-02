from django.contrib import admin

from Auth.models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("username","first_name", "last_name", "last_login", "is_staff", "is_active",)
    list_filter = ("username", "first_name", "is_active", "is_staff")