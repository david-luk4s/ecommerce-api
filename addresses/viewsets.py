from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Address
from .serializers import AddressSerializer
from perfil.permissions import ObjectPermission


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated, ObjectPermission]
