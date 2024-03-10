from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    objects = None
    title = models.CharField(max_length=70)
    genres = models.CharField(max_length=70)
    year = models.CharField(max_length=70)
    image = models.ImageField(upload_to="movie_images")
    movieduration = models.CharField(max_length=70)
    trailerlink = models.CharField(max_length=250)

    def __str__(self):
        return self.title



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    def __str__(self):
        return self.user.username
