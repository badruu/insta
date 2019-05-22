from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Image(models.Model):
    img = models.ImageField(default='leopard.jpg', upload_to='images')
    img_name = models.CharField(default='My Photo', max_length = 30)
    img_caption = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)


    def __str__(self):
        return self.img_name

    @classmethod
    def search_by_img_name(cls,search_term):
        photo = cls.objects.filter(img_name__icontains=search_term)
        return photo

    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'pk': self.pk})

    # def was_published_recently(self):
    #     return self.date_posted >= timezone.now() - datetime.timedelta(days=1)

    #solves for me the error 'improperly configured' with suggestion
    #No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.

class ImageVote(models.Model):

    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    voted = models.ForeignKey(Image, on_delete=models.CASCADE)
    published_date = models.DateField(auto_now_add=True, null=True)

    class Meta:
        unique_together = ('voter', 'voted')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.voter

# class Choice(models.Model):
#     image = models.ForeignKey(Image, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.choice_text

class Comment(models.Model):
    comment = models.TextField()
    commentor = models.ForeignKey(User, on_delete=models.CASCADE)
    date_commented = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'pk': self.pk})