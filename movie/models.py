from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    # many reviews-to-one user: user can create many reviews
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # many reviews-to-one movie: movie can have many reviews
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watchAgain = models.BooleanField()

    def __str__(self):
        return self.text