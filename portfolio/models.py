from django.db import models

# Create your models here.
class Portfolio(models.Model):
    service = models.CharField(max_length=100, null=True)
    link = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='pics', null=True)
    date = models.DateTimeField(auto_now=True)
