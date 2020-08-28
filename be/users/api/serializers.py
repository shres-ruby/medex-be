from django.db import transaction

from rest_framework import serializers

from users.models import CustomUser, Patient, Doctor, Prescription


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
   

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ('user', 'title', 'image', 'upload_date')

# class LoginSerializer(serializers.Serializer):
#     email = serializers.CharField(max_length= 100)
#     password = serializers.Charfield(max_length= 100)

#     def validate(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError("Incorrect credentials")