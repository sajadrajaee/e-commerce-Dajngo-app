from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _

# ----------- manager ---------
class CustomManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("email or phone number must be set")
        
        email = self.normalize_email(username)
        user = None
        try:
            email = CustomUser.objects.get(email=username)
        except CustomUser.DoesNotExist:
            try:
                phone = CustomUser.objects.get(phone_number = username)
            except CustomUser.DoesNotExist:
                pass
        
        if user is None:
            user = self.model(
                email=email,
                phone_number = username if not email else None
            )
            user.set_password(password)
            user.save()
            return user
        
    def create_superuser(self, username, password=None):
        user = self.create_user(username=username, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
    
# ----------------- model class -----------------
class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = " کاربر"
        verbose_name_plural = "کاربران"
        
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=180)
    username = models.CharField(max_length=150)    
    phone_number = models.IntegerField(
        null=True, blank=True, verbose_name="شماره تماس", unique=True
    )
    email = models.EmailField(_("email address"), blank=True, unique=True)
    
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = "phone_number"
    
    objects = CustomManager()
    def __str__(self):
        return self.username