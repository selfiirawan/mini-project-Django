from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(default=0, null=True, blank=True)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, null=True, blank=True)
    description = models.CharField(max_length=600, null=True, blank=True)
    image = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_genres(self):
        return self.genre.split(",")

class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=600, null=True, blank=True)
    image = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name} - {self.role}"
    
class Product(models.Model):
    image = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Studio(models.Model):
    name = models.CharField(max_length=120, unique=True)
    city = models.CharField(max_length=80)
    specialty = models.CharField(max_length=80)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)