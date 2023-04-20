from django.db import models


# Create your models here.
class CustomerMessageQuote(models.Model):
    name = models.CharField(max_length=100, null=True)
    service = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20,null=True)
    message = models.CharField(max_length=250, null=True)
    date = models.DateTimeField(auto_now=True)



