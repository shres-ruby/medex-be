from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import (CategoryListView, ProductListView, OrderQuantityUpdateView,
AddToCartView, ShoppingCartListView, ShoppingCartDeleteView, OrderListView)


r = DefaultRouter()
r.register('categories', CategoryListView)
r.register('allproducts', ProductListView)
r.register('shoppingcart', ShoppingCartListView)
r.register('myorder', OrderListView)

urlpatterns = [
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    path('order-item/update-quantity/', OrderQuantityUpdateView.as_view(),
    name='order-item-update-quantity'),
    path('order-item/<pk>/delete/', ShoppingCartDeleteView.as_view(),
    name='order-item-delete'),
] + r.urls