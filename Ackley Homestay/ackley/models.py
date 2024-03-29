from django.db import models
from django.db.models.deletion import CASCADE
from PIL import Image
from django_resized import ResizedImageField
# Create your models here.

class Contacts(models.Model):       
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Phone_Number=models.CharField(max_length=10,default='not given')
    Message=models.TextField(max_length=200)
    date=models.DateTimeField('date added')
    def __str__(self):
        return self.Name

class Bookings(models.Model):
    First_name=models.CharField(max_length=20)
    Last_name=models.CharField(max_length=20)
    Phone_number=models.CharField(max_length=10)
    Email=models.EmailField()
    Date=models.DateField('Date booked')
    Arrival=models.DateField()
    No_of_guests=models.IntegerField()
    No_of_days=models.IntegerField()
    Booking_id=models.CharField(max_length=6)
    def __str__(self):
        return self.First_name+' '+self.Last_name

class Album(models.Model):
    Img=ResizedImageField(size=[294, 225],upload_to='static/images')
    Img_name=models.CharField(max_length=20)
    Img_description=models.TextField()
    def __str__(self) -> str:
        return self.Img_name
    
