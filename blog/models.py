from django.db import models
from datetime import datetime

# Create your models here.

class Blog(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    writter= models.CharField(max_length=255)
    writter_social = models.CharField(max_length=255)
    heading = models.CharField(max_length=255,blank=True)
    content = models.TextField()
    photo = models.ImageField(upload_to='media/blog/%Y/%m')
    pub_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title