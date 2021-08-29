from django.db import models

# Create your models here.

class Centers(models.Model):
    Email=models.EmailField(max_length=30)
    Center_name=models.CharField(max_length=30)
    Center_id=models.IntegerField()
    y=models.CharField(max_length=1)

class Otp(models.Model):
    Email=models.EmailField(max_length=30)
    OTP=models.IntegerField()
    Time=models.TimeField()
