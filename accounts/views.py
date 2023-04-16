from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import serializers

from .backend import SEGUsuarioBackend
from .models import SEGUsuario


class SEGUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEGUsuario
        fields = ['US_Login', 'US_Password']


class LoginView(APIView):
    permission_classes = [AllowAny]
    queryset = SEGUsuario.objects.all()

    def post(self, request, format=None):
        serializer = SEGUsuarioSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['US_Login']
            password = serializer.validated_data['US_Password']
            user = SEGUsuarioBackend().authenticate(request, username=username, password=password)
            if user:
                user.generate_auth_token()
                return Response({'token': user.remember_token})
            else:
                return Response({'error': 'Credenciales invalidas'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
