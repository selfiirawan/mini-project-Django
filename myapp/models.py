from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(default=0, null=True, blank=True)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, null=True, blank=True)

    def __str__(self):
        return self.title

# title
# year
# genre
# director
# rating