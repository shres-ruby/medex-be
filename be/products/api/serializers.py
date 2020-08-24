from rest_framework import serializers

from products.models import (Category, Medicines, AyurvedicMedicines,
HealthSupplements, DailyEssentials, ShoppingCart, Order)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class MedicinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicines
        fields = ('title','image','description','category','price')


class AyurvedicSerializer(serializers.ModelSerializer):
    class Meta: 
        model = AyurvedicMedicines
        fields = ('title','image','description','category','price')


class SupplementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthSupplements
        fields = ('title','image','description','category','price')


class EssentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyEssentials
        fields = ('title','image','description','category','price')


class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ('user','medicines','ayurvedic','supplements','essentials',
        'quantity','purchased','created_at')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('user','orderitems','order_placed','created')