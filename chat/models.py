
from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=700)

class Message(models.Model):
    value= models.CharField (max_length=10000000)
    date= models.DateField(default=datetime.now,blank=True)
    user=models.CharField(max_length=50000000)
    room= models.CharField(max_length=509999)
    
