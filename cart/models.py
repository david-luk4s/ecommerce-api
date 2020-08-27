from django.db import models
from perfil.models import User
from products.models import Product
from addresses.models import Address


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product_id = models.ManyToManyField(Product, verbose_name='Produto')
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    date_register = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Carrinho'
        verbose_name_plural = 'Carrinhos'


class Ordens(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    total = models.DecimalField('Total', max_digits=10, decimal_places=2)
    payment_type = models.ForeignKey('PaymentType' ,verbose_name = 'Tipo de Pagamento', on_delete=models.PROTECT)
    date_register = models.DateTimeField(auto_now_add=True)


class PaymentType(models.Model):
    name = models.CharField('Nome', max_length=50)
    tipo = models.CharField('Tipo', max_length=100)

    class Meta:
        verbose_name = 'Tipo Pagamento'
        verbose_name_plural = 'Tipos de Pagamentos'
