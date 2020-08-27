from django.contrib import admin
from .models import Cart, Ordens, PaymentType


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass

@admin.register(Ordens)
class OrdensAdmin(admin.ModelAdmin):
    pass

@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    pass
