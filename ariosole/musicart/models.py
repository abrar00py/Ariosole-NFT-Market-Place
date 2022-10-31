from django.db import models

# Create your models here.
class musicart(models.Model):
    name = models.CharField( max_length=100)
    music = models.FileField(upload_to='music')
    image = models.ImageField( upload_to='musicimage')

    def __str__(self):
        return self.name
    