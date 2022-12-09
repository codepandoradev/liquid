from rest_framework import serializers
from .models import User
from .models import Token
from .models import EmailVerificationCode

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["login","password","user_email","phone_number","client_name"]

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ["login","password","user_email","phone_number","client_name"]
        



class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ["token","user_id"]
        
        
class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailVerificationCode
        fields = ["code"]
        
        
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["login","password"]
        
        
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["nickname","profile_description","user_avatar"]
        

        
