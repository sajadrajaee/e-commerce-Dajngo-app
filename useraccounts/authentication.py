from .models import CustomUser
from django.db.models import Q

class EmailAuthBackend:
    """
    custom authentication backend that allows users
    to login using there email address
    """
    def authenticate(self, username=None, password=None):
        """  this lets user to login using there email or username  """
        try:
            user = CustomUser.objects.get(Q(email=username) | Q(phone_number=username))
            if user.check_password(password):
                return user
            return None
        except CustomUser.DoesNotExist:
            return None
                
    def get_user(self, user_id):
        """ override the get user model to make users log in there phone or email"""
        try:
            return CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return None
        