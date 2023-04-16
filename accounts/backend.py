from django.contrib.auth.backends import BaseBackend
from rest_framework.permissions import AllowAny

from .models import SEGUsuario


class SEGUsuarioBackend(BaseBackend):
    permission_classes = [AllowAny]

    def authenticate(self, request, username=None, password=None):
        try:
            user = SEGUsuario.objects.get(US_Login=username, US_Password=password)
            if user is not None:
                return user
        except SEGUsuario.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return SEGUsuario.objects.get(pk=user_id)
        except SEGUsuario.DoesNotExist:
            return None
