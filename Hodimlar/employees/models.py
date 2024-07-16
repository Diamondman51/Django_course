from django.db import models

# Create your models here.

class Employee1(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hodimlar')
    job = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    tel = models.CharField(max_length=100)
    entered_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
