from django.urls import path
from .views import *
urlpatterns=[
    path('create-user/',UserCreation.as_view()),
    path('create-profile/',CreateProfile.as_view()),
    path('get-all-user/',GetAllUser.as_view()),
    path('create-product/',CreateProduct.as_view()),
    path('upload-product-images/',UploadProductImages.as_view()),
    path('get-all-products/',GetAllProducts.as_view()),
    path('send-otp/',SendOtpOnMail.as_view()),
    path('otp-verify/',OtpVerification.as_view()),
    path('add-product-into-cart/',AddProductIntoCart.as_view()),
]