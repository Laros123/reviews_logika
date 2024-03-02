from django.db import models

# Create your models here.

class Review(models.Model):
    username = models.CharField(max_length=127)
    text = models.TextField()
    date= models.DateField(auto_now=True)
