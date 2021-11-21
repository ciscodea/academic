"""Users admin module"""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from api.users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
    )
    list_filter = ("is_staff", "created_at", "updated_at")
