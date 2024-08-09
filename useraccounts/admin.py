from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    #used to display items in userchange form of django admin panel
    fieldsets =  (
        ("user info", {"fields" : ("username", "first_name", "last_name", "email", "password" )}),
        (
            "permision", {"fields": ("is_active", "is_staff", "groups", "user_permissions")}
        )        
    )
    #used to display items in user creation form of django admin panel
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "date_joined",
                "username",
                "first_name",
                "last_name",
                "email",
                "password1",
                "password2",
                "groups",
                "user_permissions"
                )
            }
        ),
    )  

    ordering = ('date_joined',)
    list_display = [
        'username',
        'email',
        'is_active',
        'is_staff',
    ]
    list_filter = ['date_joined',]
    search_fields  = ["email", "username"]

admin.site.register(CustomUser, CustomUserAdmin)