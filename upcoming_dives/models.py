from django.db import models
from django.urls import reverse


class Upcoming_Dives(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='upcoming_dive_images')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-home', kwargs={'pk': self.pk})
