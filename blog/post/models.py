from django.db import models
from datetime import datetime
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(100000000)
    image = models.ImageField(upload_to='image/',null=True,blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    file = models.FileField(upload_to='file/',null=True,blank=True)