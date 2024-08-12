from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django import forms
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = ( #this items are going to apear in user change form
        (
            "user information", {
                "fields":("username", "first_name", "last_name", "email", "phone_number", "password")
            }
        ),
        (
            "permissions", {
                "fields": ("is_active", "is_staff", "groups", "user_permissions")
            }
        )
    )
    
    add_fieldsets = ( #this items are going to appear in user create form on admin panel
        (
            None, {
                "classes":("wide",),
                "fields" : (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "phone_number",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                )
            }
        ),
    )