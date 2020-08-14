from django.urls import path,include

from rest_framework.routers import DefaultRouter

from .views import UserListView, UserDetailView, PatientListView, DoctorListView


r = DefaultRouter()
r.register('allusers', UserListView)
r.register('patients', PatientListView)
r.register('doctors', DoctorListView)

urlpatterns=[
    
] + r.urls