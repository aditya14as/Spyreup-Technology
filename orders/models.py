from datetime import date
from django.db import models
from datetime import datetime
# Create your models here.
class Order(models.Model):
    order_choices = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ) 

    name = models.CharField(max_length=400)
    email = models.CharField(max_length=400)
    phone = models.CharField(max_length=200)
    plan = models.CharField(max_length=400)
    payment_id = models.CharField(max_length=400)
    amount = models.CharField(max_length=400)
    user_id = models.IntegerField(null=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)
    paid = models.BooleanField(default=False)
    order_status = models.CharField(choices=order_choices,max_length=50,default='Pending')
