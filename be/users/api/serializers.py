from rest_framework import serializers
from users.models import CustomUser, Patient, Doctor


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
    # user = UserSerializer(required = True)
    # user = serializers.RelatedField(read_only=True, many= True)

    class Meta:
        model = Doctor
        fields = ('user','first_name','last_name','phone','specialty','availability')