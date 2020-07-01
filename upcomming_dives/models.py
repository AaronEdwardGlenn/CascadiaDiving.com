from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class UpcommingDivePost(models.Model):
    title = models.CharField(max_length=100)
    dive_site = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class UpcommingDivePostImage(models.Model):
    property = models.ForeignKey(UpcommingDivePost, related_name='images',
                                 on_delete=models.SET(get_sentinel_user))
    image = models.ImageField()
