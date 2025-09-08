
from django.shortcuts import render
from datetime import datetime
from myapp.models import Movie
# Create your views here.

def home(request):

    # fetch all records from the Movie model
    movies = Movie.objects.all()
    
    # Steps:
        # (in future) 1 - get data from database

    # 2 - give data to html
    context = {
        "last_update": datetime.now(),
        "foods": ["Burger", "Pizza", "Pasta", "Sushi", "Nasi Goreng", "Dessert"],
    }
    #     "movies": [
    #         {
    #             "title": "Twilight",
    #             "genre": ["Fantasy", "Drama", "Romance"],
    #             "director": "Catherine Hardwicke",
    #             "year": 2008,
    #             "description": "When Bella Swan moves to a small town in the Pacific Northwest, she falls in love with Edward Cullen, a mysterious classmate who reveals himself to be a 108-year-old vampire.",
    #             "rating": 5.3,
    #         },
    #         {
    #             "title": "Harry Potter and The Goblet of Fire",
    #             "genre": ["Fantasy", "Adventure", "Family", "Mystery"],
    #             "director": "J.K. Rowling",
    #             "year": 2005,
    #             "description": "Harry Potter finds himself competing in a hazardous tournament between rival schools of magic, but he is distracted by recurring nightmares.",
    #             "rating": 7.7,
    #         },
    #         {
    #             "title": "Escape Room",
    #             "genre": ["Action", "Psychological Thriller", "Suspense Mystery"],
    #             "director": "Adam Robitel",
    #             "year": 2019,
    #             "description": "Six strangers find themselves in a maze of deadly mystery rooms and must use their wits to survive.",
    #             "rating": 6.4,
    #         },
    #     ],
    # }
    # 3 (go to home.html) - use data on html


    return render(request, 'myapp/home.html', {"movies": movies, **context})
