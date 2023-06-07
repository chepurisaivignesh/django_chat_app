from django.db import models
from datetime import datetime

# Create your models here.
class Message(models.Model):
    roomcode=models.CharField(max_length=50,blank=True,null=True)
    messenger=models.CharField(max_length=50,blank=True,null=True)
    content=models.CharField(max_length=1000,blank=True,null=True)
    message_time=models.DateTimeField(default=datetime.now(),blank=True)

class Room(models.Model):
    roomcode=models.CharField(max_length=50,blank=True,null=True)

