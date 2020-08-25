from rest_framework import serializers

from products.models import Category, Product, ShoppingCart, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title','image','description','category','price')


class ShoppingCartSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = ShoppingCart
        fields = ('user', 'item', 'quantity','ordered','created_at',
        'total_price')
    
    def get_total_price(self, obj):
        return obj.get_total_price()


class OrderSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('user','items','ordered','created', 'total')

    def get_total(self, obj):
        return obj.get_total()