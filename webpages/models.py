from django.db import models
from datetime import datetime
# Create your models here.
class Slider(models.Model):

    sliderId_choices = (
        ('slider1', 'slider1'),
        ('slider2', 'slider2'),
        ('slider3', 'slider3'),
    ) 
    headline = models.CharField(choices=sliderId_choices,max_length=50,default=True)
    photo = models.ImageField(upload_to='media/silder/%Y')
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.headline


class Plan(models.Model):
    plan_choice = (
        ('Basic', 'Basic'),
        ('Standard', 'Standard'),
        ('Premium', 'Premium'),
    )
    plan_types = models.CharField(choices=plan_choice,max_length=50)
    originalprice = models.CharField(max_length=50,default=True)
    price = models.CharField(max_length=50)
    discountpercent = models.CharField(max_length=50,default=True)

    def __str__(self):
        return self.plan_types

