from rest_framework import viewsets

from users.models import CustomUser, Patient, Doctor
from .serializers import UserSerializer, PatientSerializer, DoctorSerializer

class UserListView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetailView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class PatientListView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    # def get(self, format=None):
    #     patients = Patient.objects.all()
    #     serializer = PatientSerializer(patients, many=True)
    #     return Response(serializer.data)

class DoctorListView(viewsets.ModelViewSet):
    # def get(self, format=None):
    #     doctors = Doctor.objects.all()
    #     serializer = PatientSerializer(doctors, many=True)
    #     return Response(serializer.data)
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
