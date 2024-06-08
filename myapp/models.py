from django.db import models

class currency_model(models.Model):
    names = models.CharField(max_length = 100,null=False,blank=False)