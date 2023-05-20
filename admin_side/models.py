from django.db import models
from django.forms import ModelForm

# Create your models here.
class sign_up(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    image = models.FileField(upload_to='./sign_up_profile/',default='')

class SIGN_UP(ModelForm):
    class Meta:
        model = sign_up
        fields = ['name','email','password','image']
        
class team(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    image = models.FileField(upload_to='./team/',default='')

class TEAM(ModelForm):
    class Meta:
        model = team
        fields = ['name','designation','image']

class car_category(models.Model):
    name = models.CharField(max_length=90)
    discription = models.CharField(max_length=550)
    image = models.FileField(upload_to='./car_category/',default='')
    def __str__(self) -> str:
        return self.name
    
class CAR_CATEGORY(ModelForm):
    class Meta:
        model = car_category
        fields = ['name','discription','image']

class brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='./brand_image',default='')
    def __str__(self) -> str:
        return self.name

class BRAND(ModelForm):
    class Meta:
        model = brand
        fields = ['name','image']

class car(models.Model):
    name = models.CharField(max_length=60)
    prize = models.BigIntegerField()
    discription = models.CharField(max_length=500)
    category = models.ForeignKey(car_category,on_delete=models.CASCADE)
    car_brand = models.ForeignKey(brand,on_delete=models.CASCADE)
    person = models.BigIntegerField()
    music = models.CharField(max_length=50)
    ac = models.CharField(max_length=50)
    fuel = models.CharField(max_length=50)
    image = models.FileField(upload_to='./car_image/', default='')

class CAR(ModelForm):
    class Meta :
        model = car
        fields = ['name', 'prize', 'discription', 'category','car_brand', 'person', 'music', 'ac', 'fuel', 'image']
