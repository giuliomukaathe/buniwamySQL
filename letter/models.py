from django.db import models

# Create your models here.
class Subscribers(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    second_name = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=50, null=True)
    region = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now=True)


class MailMessage(models.Model):
    title = models.CharField(max_length=100, null=True,)
    message = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)
