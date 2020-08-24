from django.contrib import admin
from .models import (Medicines, AyurvedicMedicines, HealthSupplements, 
DailyEssentials, Category, ShoppingCart, Order)


admin.site.register(Medicines)
admin.site.register(AyurvedicMedicines)
admin.site.register(HealthSupplements)
admin.site.register(DailyEssentials)
admin.site.register(Category)
admin.site.register(ShoppingCart)
admin.site.register(Order)