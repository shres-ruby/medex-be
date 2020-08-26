from django.shortcuts import get_object_or_404

from rest_framework import generics, viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from products.models import Category,Product, ShoppingCart, Order
from .serializers import (CategorySerializer, ProductSerializer, 
ShoppingCartSerializer, OrderSerializer)
from .pagination import CustomPagination


class CategoryListView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(viewsets.ModelViewSet):
    permissions_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]

    search_fields = ['title','category__title','description']
    order_fields = ['category']
    filterset_fields = ['title']


class OrderQuantityUpdateView(APIView):
    def post(self, request, *args, **kwrgs):
        title = request.data.get('title', None)

        if title is None:
            return Response({"message": "Invalid data"}, status= HTTP_400_BAD_REQUEST)
        item = get_object_or_404(Product, title=title)
        order_status = Order.objects.filter(user=request.user, ordered=False)
        
        if order_status.exists():
            order = order_status[0]
            if order.items.filter(item__title=item.title).exists():
                order_item = ShoppingCart.objects.filter(item=item,
                user=request.user, ordered=False)[0]
                
                if order_item.quantity > 1:
                    order_item.quantity -= 1
                    order_item.save()
                else:
                    order.items.remove(order_item)
                return Response(status=HTTP_200_OK)
            else:
                return Response({"message": "This item was not in your cart"},
                status=HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "You do not have an active order"},
            status = HTTP_400_BAD_REQUEST)


class AddToCartView(APIView):
    def post(self, request, *args, **kwargs):
        title = request.data.get('title', None)
        if title is None:
            return Response({"message": "Invalid request"}, status=HTTP_400_BAD_REQUEST)

        item = get_object_or_404(Product, title=title)

        order_item_status = ShoppingCart.objects.filter(item=item,
        user=request.user, ordered=False)

        if order_item_status.exists():
            order_item = order_item_status.first()
            order_item.quantity += 1
            order_item.save()

        else:
            order_item = ShoppingCart.objects.create(item=item,
            user=request.user, ordered=False)
            order_item.save()

        order_status = Order.objects.filter(user=request.user, ordered=False)
        if order_status.exists():
            order = order_status[0]
            if not order.items.filter(item__id=order_item.id).exists():
                order.items.add(order_item)
                return Response(status=HTTP_200_OK)
        
        else:
            order = Order.objects.create(user=request.user)
            order.items.add(order_item)
            return Response(status=HTTP_200_OK)

class ShoppingCartListView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication,]
    permissions_classes = [IsAuthenticated,]
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer


class ShoppingCartDeleteView(generics.DestroyAPIView):
    permissions_classes = [IsAuthenticated]
    queryset = ShoppingCart.objects.all()


class OrderListView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication,]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer