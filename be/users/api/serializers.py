from django.db import transaction

from rest_framework import serializers
from rest_framework.fields import ListField

from users.models import (CustomUser, Patient, Doctor, Prescription,
HealthProfile)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email','is_patient','is_doctor')

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer(required = True)

    class Meta:
        model = Patient
        fields = ('user','first_name','last_name','dob','address','phone')
    

class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ('user','first_name','last_name','phone','specialty','availability')


class PatientSignupSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    dob = serializers.DateField(required=True)
    address = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ('email','password', 'password2','first_name','last_name','dob','address','phone')
        extra_kwargs = {'password': {'write_only': True}}
    
    @transaction.atomic
    def save(self):
        user = CustomUser(
            email= self.validated_data['email'],
        )
        password = self.validated_data['password']
        user.is_patient =  True
        user.set_password(password)
        user.save()
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


class ProfileSerializer(serializers.ModelSerializer):
    user = PatientSerializer(required = True)
    user = serializers.EmailField(source='user.user.email')
    doctor = serializers.StringRelatedField(many=True)
    class Meta:
        model = HealthProfile
        fields = ('user', 'name', 'height', 'weight', 'blood_pressure',
        'health_conditions', 'doctor')
        lookup_field = 'user'


# class StringArrayField(ListField):
#     """
#     String representation of an array field.
#     """
#     def to_representation(self, obj):
#         # obj = super().to_representation(self, obj)
#         # convert list to string
#         return ",".join([str(element) for element in obj])

#     def to_internal_value(self, data):
#         data = data.split(",")  # convert string to list
#         return super().to_internal_value(self, data)


class EditProfileSerializer(serializers.ModelSerializer):
    # user = serializers.EmailField(source='user.user.email')
    name = serializers.CharField()
    height = serializers.CharField(default=None)
    weight = serializers.CharField(default=None)
    blood_pressure = serializers.CharField(default=None)
    health_conditions = serializers.CharField(default=None)
    doctor = DoctorSerializer(default=None, many=True) 
    # doctor = StringArrayField()

    class Meta:
        model = Patient
        fields = ('user', 'name', 'height', 'weight', 'blood_pressure',
        'health_conditions', 'doctor')
       
    @transaction.atomic
    def save(self):
        user = Patient(
            user = self.validated_data['user']
        )
        user.save()
        profile = HealthProfile.objects.create(user=user)
        profile.name = self.validated_data['name']
        profile.height = self.validated_data['height']
        profile.weight = self.validated_data['weight']
        profile.blood_pressure = self.validated_data['blood_pressure']
        profile.health_conditions = self.validated_data['health_conditions']
        profile.save()
        profile.doctor.set(self.validated_data['doctor'])
        profile.save()
        return user
   

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ('user', 'title', 'image', 'upload_date')


    