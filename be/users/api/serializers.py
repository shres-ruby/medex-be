from django.db import transaction

from rest_framework import serializers
from rest_framework.fields import ListField

from users.models import (CustomUser, Patient, Doctor, Prescription,
HealthProfile, Appointment)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email','is_patient','is_doctor')


class PrescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prescription
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    depth = 1

    class Meta:
        model = Patient
        fields = "__all__"


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer(required = True)

    class Meta:
        model = Doctor
        fields = ('user','first_name', 'last_name', 'phone', 'specialty', 
        'availability', 'appointments', 'profile')
        extra_kwargs = {'profile': {'required': False},
                        'appointments': {'required': False}}


class AppointmentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=Patient.objects.all(),slug_field='user__email')
    doctor = serializers.SlugRelatedField(queryset=Doctor.objects.all(),slug_field='user__email')

    class Meta: 
        model = Appointment
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    depth = 1
    
    class Meta:
        model = HealthProfile
        fields = ('user','full_name','height','weight','blood_pressure','health_conditions')
        extra_kwargs = {'doctor': {'required': False}}
        lookup_field = 'user'


class PatientSignupSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    dob = serializers.DateField(required=True)
    address = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    full_name = serializers.CharField(required=True)
    height = serializers.CharField(required=False)
    weight = serializers.CharField(required=False)
    blood_pressure = serializers.CharField(required=False)
    health_conditions = serializers.CharField(required=False)
    doctor = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ('email','password', 'password2','first_name',
        'last_name','dob','address','phone','full_name','height', 
        'weight','blood_pressure','health_conditions','doctor')
        extra_kwargs = {'password': {'write_only': True}, 'password2': {'write_only': True}}
    
    @transaction.atomic
    def save(self):
        user = CustomUser(
            email= self.validated_data['email'],
        )
        password = self.validated_data['password']
        user.is_patient =  True
        user.set_password(password)
        user.save()
        profile = HealthProfile.objects.create(user=user)
        profile.full_name = self.validated_data['full_name']
        profile.height = self.validated_data['height']
        profile.weight = self.validated_data['weight']
        profile.blood_pressure = self.validated_data['blood_pressure']
        profile.health_conditions = self.validated_data['health_conditions']
        profile.doctor = self.validated_data['doctor']
        profile.save()
        patient = Patient.objects.create(user=user)
        patient.first_name = self.validated_data['first_name']
        patient.last_name = self.validated_data['last_name']
        patient.dob = self.validated_data['dob']
        patient.address = self.validated_data['address']
        patient.phone = self.validated_data['phone']
        patient.save()
        return user


class DoctorSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    specialty = serializers.CharField(required=True)
    availability = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ('email','password', 'password2','first_name','last_name','phone','specialty','availability')
        extra_kwargs = {'password': {'write_only': True}}
    
    @transaction.atomic
    def save(self):
        user = CustomUser(
            email= self.validated_data['email'],
        )
        password = self.validated_data['password']
        user.is_doctor =  True
        user.set_password(password)
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.first_name = self.validated_data['first_name']
        doctor.last_name = self.validated_data['last_name']
        doctor.phone = self.validated_data['phone']
        doctor.specialty = self.validated_data['specialty']
        doctor.availability = self.validated_data['availability']
        doctor.save()
        return user


