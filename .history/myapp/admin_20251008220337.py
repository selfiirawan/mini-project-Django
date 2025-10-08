from django.contrib import admin
from myapp.models import Movie, Food, TeamMember

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

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "image",
    ]

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "age",
        "role",
        "is_active",
    ]