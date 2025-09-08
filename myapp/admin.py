from django.contrib import admin
from myapp.models import Movie

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "year",
        "genre",
        "director",
        "rating",
        "description",
        "image",
    ]