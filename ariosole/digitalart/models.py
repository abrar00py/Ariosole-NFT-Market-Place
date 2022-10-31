from django.db import models

# Create your models here.

class digitalart(models.Model):
    name=models.CharField( max_length=100)
    image=models.ImageField()

    def __str__(self):
        return self.name
    