from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Cart, Ordens, PaymentType
from .serializers import CartSerializer, OrdensSerializer, PaymentTypeSerializer
from perfil.permissions import ObjectPermission


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, ObjectPermission]


class OrdensViewSet(viewsets.ModelViewSet):
    queryset = Ordens.objects.all()
    serializer_class = OrdensSerializer
    permission_classes = [IsAuthenticated, ObjectPermission]


class PaymentTypeViewSet(viewsets.ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer
    permission_classes = [IsAuthenticated, ObjectPermission]