from django.db import models

class sumemrPhoto(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50)
    photo = models.ImageField(blank=True, upload_to="image")