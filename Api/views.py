from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random
from django.core.mail import send_mail

# Create your views here.

def generate_unique_id(pre_fix):
    unique_id=random.randint(10000,99999)
    return str(pre_fix+'-'+str(unique_id))
class UserCreation(APIView):
    def post(self,request,*args,**kwargs):
        serializers=UserSerializers(data=request.data)
        if serializers.is_valid():
            user=serializers.save()
            user.set_password(user.password)
            data={
                'message':'Success',
                'status' : status.HTTP_200_OK,
            }
            return Response(data)
        return Response(data=serializers.errors)

class CreateProfile(APIView):
    def post(self, request, *args, **kwargs):
        serializers = UserProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            data = {
                'message': 'Success',
                'status': status.HTTP_200_OK,
            }
            return Response(data)
        return Response(data=serializers.errors)

class GetAllUser(APIView):
    def get(self, request, *args, **kwargs):
        records=User.objects.all()
        serializers = GetUserSerializer(records,many=True)
        return Response(data=serializers.data)

class CreateProduct(APIView):
    def post(self, request, *args, **kwargs):
        serializers = ProductMainTableSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save(unique_id=generate_unique_id('PID'))
            data = {
                'message': 'Success',
                'status': status.HTTP_200_OK,
            }
            return Response(data)
        return Response(data=serializers.errors)
class UploadProductImages(APIView):
    def post(self, request, *args, **kwargs):
        serializers = ProductImageModelSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            data = {
                'message': 'Success',
                'status': status.HTTP_200_OK,
            }
            return Response(data)
        return Response(data=serializers.errors)

class GetAllProducts(APIView):
    def get(self, request, *args, **kwargs):
        records=ProductImageModel.objects.all()
        serializers = GetAllProductSerializer(records,many=True)
        return Response(data=serializers.data)

class SendOtpOnMail(APIView):
    def post(self, request, *args, **kwargs):
        serializers = SendOtpSerialiser(data=request.data)
        if serializers.is_valid():
            serializers=serializers.data
            email=serializers['email']
            otp = random.randint(100000, 999999)
            request.session['OTP'] = str(otp)
            subject = "OTP Verification"
            message = f"Dear , customer verify the otp,your otp is {otp}"
            mail_from = 'ram.bharathbrands@gmail.com'
            send_mail(
                subject,
                message,
                mail_from,
                [email],
                fail_silently=False
            )
            data = {
                'message': 'Success',
                'detail_message': 'Check your email and use this endpoint to verify the otp "verify otp" ',
                'status': status.HTTP_200_OK,
            }
            return Response(data)
        return Response(data=serializers.errors)


class OtpVerification(APIView):
    def post(self, request, *args, **kwargs):
        serializers = EnterOptSerializer(data=request.data)
        if serializers.is_valid():
            serializers=serializers.data
            otp=serializers['otp']
            OTP=request.session['OTP']
            print(otp,OTP)
            if str(otp) == str(OTP):
                data = {
                    'message': 'Success',
                    'detail_message': 'your provided otp is correct...Carry one next...Welcome',
                    'status': status.HTTP_200_OK,
                }
                return Response(data)
            else:
                data = {
                    'message': 'Failure',
                    'detail_message': 'your provided otp is incorrect...please recheck...',
                    'status': status.HTTP_400_BAD_REQUEST,
                }
                return Response(data)

        return Response(data=serializers.errors)

class AddProductIntoCart(APIView):
    def post(self, request, *args, **kwargs):
        serializers = UserCartProductModelSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            data = {
                'message': 'Success',
                'detail_message': 'Product Added into the cart',
                'status': status.HTTP_200_OK,
            }
            return Response(data)

        return Response(data=serializers.errors)
