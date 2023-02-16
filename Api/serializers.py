from TechArionApp.models import *
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email','phone_number','is_customer','is_admin']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields='__all__'

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email',]
class ProductMainTableSerializers(serializers.ModelSerializer):
    class Meta:
        model=ProductMainTable
        fields='__all__'
class ProductImageModelSerializers(serializers.ModelSerializer):
    class Meta:
        model=ProductImageModel
        fields='__all__'
class GetAllProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImageModel
        fields='__all__'

class SendOtpSerialiser(serializers.Serializer):
    email=serializers.EmailField()
class EnterOptSerializer(serializers.Serializer):
    otp=serializers.IntegerField()

class UserCartProductModelSerializers(serializers.ModelSerializer):
    class Meta:
        model=UserCartProductModel
        fields='__all__'
