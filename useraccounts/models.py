from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    
    def __str__(self):
        return self.first_name
    
    
# class EmailOrPhoneBackend(ModelBackend):
#     def authenticate(self, request, username=None, password = None, **kwargs):
#         UserModel = CustomUser()
#         try:
#             user = UserModel.objects.get(email = username)
#         except UserModel.DoesNotExist:
#             try:
#                 user = UserModel.objects.get(phone_number=username)
#             except UserModel.DoesNotExist:
#                 return None
#         else:
#             if user.check_password(password):
#                 return user
            