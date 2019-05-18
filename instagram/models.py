from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Image(models.Model):
    img = models.ImageField(default='leopard.jpg', upload_to='images')
    img_name = models.CharField(default='My Photo', max_length = 30)
    img_caption = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.img_name

    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'pk': self.pk})

    #solves for me the error 'improperly configured' with suggestion
    #No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.