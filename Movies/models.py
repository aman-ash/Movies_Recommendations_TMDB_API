from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=30)

    email = models.EmailField()
    number = models.CharField(max_length=10, default='')
    desc = models.TextField()

    def __str__(self):
        return self.name + ' - ' + self.email


class Movie_name(models.Model):
    movie_name = models.CharField(max_length=30)

    def __str__(self):
        return self.movie_name
