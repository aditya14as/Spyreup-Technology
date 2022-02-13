from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class extendeduser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=20,blank=True)
    auth_token = models.CharField(max_length=100,default=True )
    forget_password_token = models.CharField(max_length=100,default=True )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.user.email

