from rest_framework import generics, viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from products.models import (Category, Medicines, AyurvedicMedicines,
HealthSupplements, DailyEssentials, ShoppingCart, Order)
from .serializers import (CategorySerializer, MedicinesSerializer, AyurvedicSerializer,
SupplementsSerializer, EssentialsSerializer, ShoppingCartSerializer, OrderSerializer)



class CategoryListView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MedicinesListView(viewsets.ModelViewSet):
    queryset = Medicines.objects.all()
    serializer_class = MedicinesSerializer


class AyurvedicListView(viewsets.ModelViewSet):
    queryset = AyurvedicMedicines.objects.all()
    serializer_class = AyurvedicSerializer


class SupplementsListView(viewsets.ModelViewSet):
    queryset = HealthSupplements.objects.all()
    serializer_class = SupplementsSerializer


class EssentialsListView(viewsets.ModelViewSet):
    queryset = DailyEssentials.objects.all()
    serializer_class = EssentialsSerializer


class ShoppingCartListView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permissions_classes = [permissions.IsAuthenticated]
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer


class OrderListView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication,]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer