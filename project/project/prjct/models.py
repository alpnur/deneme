from django.db import models

# Create your models here.
class Member(models.Model):
    firstname= models.CharField(max_length= 100)
    lastname = models.CharField(max_length=100)
    phonenumber= models.CharField(max_length=11)

class Stuff (models.Model):
    stuffname= models.CharField(max_length = 100)
    member = models.ForeignKey(Member, on_delete= models.CASCADE)
