from django.db import models

# Create your models here.
class CustomerMessage(models.Model):
    name = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20,null=True)
    message = models.CharField(max_length=250, null=True)
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name 