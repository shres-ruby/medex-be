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
    class Meta:
        model = Patient
        fields = ('user','first_name','last_name','dob','address','phone')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = Patient.objects.create_user(validated_data['user'])
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