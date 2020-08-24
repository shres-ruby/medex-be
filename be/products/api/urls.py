from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import (CategoryListView, MedicinesListView, AyurvedicListView,
SupplementsListView, EssentialsListView, ShoppingCartListView, OrderListView)


r = DefaultRouter()
r.register('categories', CategoryListView)
r.register('allmedicines', MedicinesListView)
r.register('allayurvedics', AyurvedicListView)
r.register('allsupplements', SupplementsListView)
r.register('allessentials', EssentialsListView)
r.register('shoppingcart', ShoppingCartListView)
r.register('myorder', OrderListView)

urlpatterns = [

] + r.urls