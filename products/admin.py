from django.contrib import admin
from .models import Product, ImageProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(ImageProduct)
class ImageProductAdmin(admin.ModelAdmin):
    pass
