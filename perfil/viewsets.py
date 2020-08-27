from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer, PerfilTokenObtainPairSerializer
from core import settings
import jwt
from jwt.exceptions import InvalidSignatureError, InvalidTokenError
from .permissions import ObjectPermission
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ObjectPermission]


class PerfilClassTokenObtain(TokenObtainPairView):
    serializer_class = PerfilTokenObtainPairSerializer
    token_obtain_pair = TokenObtainPairView.as_view()
