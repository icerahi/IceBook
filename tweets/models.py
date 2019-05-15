from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse, reverse_lazy

from .validators import validate_content
from mdeditor.fields import MDTextField

class Tweet(models.Model):
    #user
    user= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content=MDTextField()
    updated= models.DateTimeField(auto_now_add=True)
    timestamp=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return (self.content)

    def get_absolute_url(self):
        return reverse_lazy('tweet:detail',kwargs={'pk':self.pk})

    class Meta:
        ordering=['-timestamp']
