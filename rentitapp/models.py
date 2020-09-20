from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True,related_name="profile")
    image = models.ImageField(default='profile_pics/default.jpg',upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username}.Vehicles'

class Vehicles(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    tov = models.CharField(max_length=50,default='')
    Adtitle = models.CharField(max_length=50,default='')
    brand = models.CharField(max_length=50,default='')
    cost = models.IntegerField()
    DOM = models.IntegerField()
    S_desc = models.CharField(max_length=150,default='')
    status =models.BooleanField(default=False)
    img1 = models.ImageField(upload_to='vehicles')
    def __str__(self):
        return f'{self.user.username}.Vehicles'




class Apartments(models.Model):
    toa = models.CharField(max_length=50,default='')
    Adtitle = models.CharField(max_length=50)
    bedroom = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    carpet_area = models.CharField(max_length=50)
    floors = models.CharField(max_length=50)
    cost = models.IntegerField()
    DOM = models.IntegerField()
    S_desc = models.CharField(max_length=150)
    img1 = models.ImageField(upload_to=None)
    img2 = models.ImageField(upload_to=None)
    img3 = models.ImageField(upload_to=None,default='')
    img4 = models.ImageField(upload_to=None,default='')
    img5 = models.ImageField(upload_to=None,default='')
    img6 = models.ImageField(upload_to=None,default='')
    img7 = models.ImageField(upload_to=None,default='')

class Electronics(models.Model):
    top = models.CharField(max_length=50,default='')
    Adtitle = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    cost = models.IntegerField()
    DOM = models.IntegerField()
    S_desc = models.CharField(max_length=150)
    img1 = models.ImageField(upload_to=None)
    img2 = models.ImageField(upload_to=None)

class Furnitures(models.Model):
    tof = models.CharField(max_length=50,default='')
    Adtitle = models.CharField(max_length=50)
    wood = models.CharField(max_length=50)
    cost = models.IntegerField()
    DOM = models.IntegerField()
    S_desc = models.CharField(max_length=150)
    img1 = models.ImageField(upload_to=None)
    img2 = models.ImageField(upload_to=None)
    img3 = models.ImageField(upload_to=None)

class Freelance(models.Model):
    tof = models.CharField(max_length=50,default='')
    Adtitle = models.CharField(max_length=50)
    cost = models.IntegerField()
    S_desc = models.CharField(max_length=50,default='')







