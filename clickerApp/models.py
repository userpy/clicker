from django.db import models

# Create your models here.
class Links(models.Model):
    code = models.CharField(max_length=250)
    url = models.CharField(max_length=250)