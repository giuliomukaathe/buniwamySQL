from django.db import models

# Create your models here.
class Testimonial(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False,verbose_name='ID')
    name = models.CharField(max_length=200)
    proffession = models.CharField(max_length=200)
    message = models.TextField()
    image = models.ImageField(upload_to='pics')