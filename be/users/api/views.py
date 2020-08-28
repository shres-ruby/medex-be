from rest_framework import generics, viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from users.models import CustomUser, Patient, Doctor, Prescription
from .serializers import (UserSerializer, PatientSerializer, DoctorSerializer,
PatientSignupSerializer, PrescriptionSerializer)
from .permissions import IsOwnerOrReadOnly, IsSuperUser, IsDoctor
from .pagination import CustomPagination

import logging


class UserListView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, ]
    # permission_classes=[IsAuthenticated,]
    # permission_classes=[IsSuperUser | IsDoctor]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]

    search_fields = ['email']
    order_fields = ['email']
    filterset_fields = ['email', 'is_patient', 'is_doctor']

    def perform_create(self, serializer):
        serializer.save(user= self.request.user)


class UserDetailView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication,]
    permission_classes= [permissions.IsAuthenticated | IsOwnerOrReadOnly]
    serializer_class = UserSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('id')
        if user_id:
            return CustomUser.objects.filter(id=user_id.first())
        return CustomUser.objects.none()



class PatientListView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication,]
    # permission_classes=[IsSuperUser | IsDoctor ]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]

    search_fields = ['first_name', 'last_name', 'phone']
    filterset_fields = ['first_name', 'last_name', 'phone']
    

class DoctorListView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]

    search_fields = ['first_name', 'last_name', 'phone']
    filterset_fields = ['first_name', 'last_name', 'phone']


class PatientSignupAPI(generics.GenericAPIView):
    serializer_class = PatientSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user" : UserSerializer(user, 
            context=self.get_serializer_context()).data,
            "token": Token.objects.create(user=user)
        })


class PrescriptionView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    # permission_classes= [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
