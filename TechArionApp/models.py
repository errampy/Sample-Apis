from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    phone_number=models.PositiveBigIntegerField(unique=True,blank=False,null=True)
    email=models.EmailField(blank=False,null=False,unique=True)
    is_customer=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)

class UserProfile(models.Model):
    owner=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,blank=False,null=False)
    date_of_birth=models.DateField(blank=False,null=False)
    GENDER=(('MALE','MALE'),('FEMALE','FEMALE'),('OTHERS','OTHERS'))
    gender=models.CharField(max_length=6,choices=GENDER)
    image=models.ImageField(upload_to='profile/')

class UserLoginOtpModel(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    opt=models.IntegerField()
    active=models.BooleanField(default=False)

class UserCartProductModel(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey('TechArionApp.ProductMainTable',on_delete=models.CASCADE)
    STATUS = (('pending', 'pending'), ('completed', 'completed'))
    status=models.CharField(max_length=9,choices=STATUS)

class ProductMainTable(models.Model):
    title=models.CharField(max_length=50,blank=False,null=False)
    description=models.TextField()
    unique_id=models.CharField(max_length=20,primary_key=True,unique=True,blank=False,null=False,editable=False)
    price=models.FloatField()

class ProductImageModel(models.Model):
    product=models.ForeignKey(ProductMainTable,on_delete=models.CASCADE)
    images=models.ImageField(upload_to='product/')

