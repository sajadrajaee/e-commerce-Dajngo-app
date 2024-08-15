from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

@admin.register(CustomUser)
class CustumUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm #form for adding user
    form = CustomUserChangeForm # for editing user
    model = CustomUser
    fieldsets = (
        (
            "userinfo", {"fields":("first_name", "last_name", "username", "email", "password"),}
        ),
    )
    add_fieldsets = (
        (
            None, {
                "classes" : ("wide",),
                "fields" : (
                    "first_name", "last_name" ,"email", "username", "password1", "password2"
                )
            }
        ),
    )
    
# admin.site.register(CustomUser, CustumUserAdmin)
