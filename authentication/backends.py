from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()
class PhoneEmailBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')
        # phone = kwargs.get('phone')
        print(email, password, phone)
        try:
            user = User.objects.get(Q(email__iexact=email))
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

