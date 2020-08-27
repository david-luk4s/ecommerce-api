from rest_framework import serializers
from .models import Cart, Ordens, PaymentType


class CartSerializer(serializers.ModelSerializer):
    date_register = serializers.DateTimeField(format='%d/%m/%Y %H:%M', required=False)

    class Meta:
        model = Cart
        fields = ('id', 'user', 'product_id', 'quantity', 'date_register')


class PaymentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentType
        fields = ('name', 'tipo')


class OrdensSerializer(serializers.ModelSerializer):
    payment_type = PaymentTypeSerializer()
    date_register = serializers.DateTimeField(format='%d/%m/%Y %H:%M')

    class Meta:
        model = Ordens
        fields = ('id', 'cart', 'address', 'total', 'payment_type', 'date_register')
