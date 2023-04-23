from django.db import models
from datetime import datetime

# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to = "myimage")
    #date = models.DateTimeField(datetime.now())