from django.contrib import admin
from .models import (Category, Product, ShoppingCart, Order)


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ShoppingCart)
admin.site.register(Order)