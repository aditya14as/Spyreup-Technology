from django.db import models
from datetime import datetime
# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    company = models.CharField(max_length=255,blank=True)
    subject = models.CharField(max_length=255,blank=True)
    message = models.TextField()
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email