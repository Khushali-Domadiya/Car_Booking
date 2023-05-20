from django.db import models
from django.forms import ModelForm

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