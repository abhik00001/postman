from django.db import models

# Create your models here.
class todo(models.Model):
    todo = models.CharField(max_length=150)
    description = models.TextField()
    date =  models.DateField(auto_now_add=True)