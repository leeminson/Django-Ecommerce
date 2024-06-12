from django.db import models
from django.utils.text import slugify
# Create your models here.
class Img(models.Model):
    image = models.ImageField(upload_to='img/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    