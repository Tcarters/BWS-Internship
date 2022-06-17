from distutils.command.upload import upload
from django.db import models
# from django.forms import ImageField

from sorl.thumbnail import ImageField

# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=140, blank=False, null=False)
    image = ImageField()
    # (upload_to='whatever')
    


    def __str__(self):
        return self.text