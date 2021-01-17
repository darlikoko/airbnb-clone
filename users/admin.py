from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# @admin.register(models.User) = admin.site.register(models.User, CustomUserAdmin)
# class CustomUserAdmin(admin.ModelAdmin):
# list_display = ("username", "gender", "email", "currency", "superhost")
# list_filter = ("gender", "language", "currency", "superhost")


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """comment"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom profile",
            {
                "fields": (
                    "avator",
                    "gender",
                    "bio",
                    "birthday",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
