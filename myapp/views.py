
from django.shortcuts import render
from datetime import datetime
from myapp.models import Movie, Food
# Create your views here.

def home(request):

    # fetch all records from the Movie model
    # will be using data from the admin panel
    movies = Movie.objects.all()
    foods = Food.objects.all()

    # Steps:
        # (in future) 1 - get data from database

    # 2 - give data to html
    context = {
        "last_update": datetime.now(),
    }
    
    # 3 (go to home.html) - use data on html

    return render(request, 'myapp/home.html', {"movies": movies, "foods": foods, **context})


def contact(request):
    return render(request, 'myapp/contact.html', {})

def about(request):
    return render(request, 'myapp/about.html', {})