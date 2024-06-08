from django.db import models

class currency_model(models.Model):
    names = models.CharField(max_length = 100,null=False,blank=False)

    def __str__(self) -> str:
        return self.names