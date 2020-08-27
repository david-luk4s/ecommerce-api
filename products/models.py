from django.db import models
from perfil.models import User
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField('Nome Produto', max_length=100)
    description = models.TextField('Descrição')
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.PROTECT)
    image = models.ManyToManyField('ImageProduct', verbose_name='Imagens', blank=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    
    def __str__(self):
        return self.name


class ImageProduct(models.Model):
    image = models.ImageField(upload_to='products', null=True, blank=True)

    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'