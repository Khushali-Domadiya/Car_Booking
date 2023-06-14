from django.db import models
from django.forms import ModelForm
from admin_side.models import *

# Create your models here.
class signup(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact = models.BigIntegerField()
    password = models.CharField(max_length=20)
    image = models.FileField(upload_to='./signup_web',default='')

class SIGNUP(ModelForm):
    class Meta:
        model = signup
        fields = ['name','email','contact','password','image']

class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=200)

class CONTACT(ModelForm):
    class Meta:
        model = contact
        fields = ['name','email','subject','message']

class booking_detail(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    pick_up = models.CharField(max_length=50)
    drop = models.CharField(max_length=50)
    pickup_date = models.CharField(max_length=50)
    drop_time = models.CharField(max_length=50)
    adult = models.IntegerField()
    child = models.IntegerField()
    request = models.CharField(max_length=500)
    payment = models.CharField(max_length=50)
    car_id = models.ForeignKey(car,on_delete=models.CASCADE)
    car_name = models.CharField(max_length=50)

class BOOKING_DETAIL(ModelForm):
    class Meta:
        model = booking_detail
        fields = ['fname','lname','email','contact','pick_up','drop','pickup_date','drop_time','adult','child','request','payment','car_id','car_name']

class review(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    message = models.CharField(max_length=500)
    profession = models.CharField(max_length=100)
    image = models.FileField(upload_to='./review_image',default='')

class REVIEW(ModelForm):
    class Meta:
        model = review
        # fields = ['name','email','message','image']
        fields = "__all__"