from django.db import models
import os
from django.conf import settings
from imagekit.models import ProcessedImageField, ProcessedImageField
from imagekit.processors import Thumbnail

class Image(models.Model):
    name = models.CharField(max_length=200)
    origin = models.ImageField('Input', upload_to='origin')
    result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    to_gallery = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}, {self.origin}'
