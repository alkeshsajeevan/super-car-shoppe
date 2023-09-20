from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f' {self.name}'


class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100,default='')
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    kilometer=models.IntegerField(default=0)
    fuel=models.CharField(max_length=100,default='null')
    location=models.CharField(max_length=100,default='thrissur')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image1 = models.ImageField(upload_to='uploads/',default='uploads/noimg.jpg')
    image2 = models.ImageField(upload_to='uploads/',default='uploads/noimg.jpg')
    image3 = models.ImageField(upload_to='uploads/',default='uploads/noimg.jpg')
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.year} {self.make} {self.name}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
