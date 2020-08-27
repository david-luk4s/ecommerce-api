from django.db import models
from perfil.models import User


class Address(models.Model):
    address = models.CharField('Endereço', max_length=100)
    number = models.CharField('Número', max_length=16)
    complement = models.CharField('Complemento', max_length=100, null=True, blank=True)
    district = models.CharField('Distrito', max_length=100, null=True, blank=True)
    city = models.CharField('Cidade', max_length=100)
    stable = models.CharField('Estado', max_length=100)
    zipcode = models.CharField('CEP', max_length=8)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'