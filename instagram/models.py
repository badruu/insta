from django.db import models
from django.utils import timezone

class Image(models.Model):
    img = models.ImageField(default='leopard.jpg', upload_to='images')
    img_name = models.CharField(default='My Photo', max_length = 30)
    img_caption = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.img_name