
from django.shortcuts import render
from datetime import datetime
from myapp.models import Movie, Food, TeamMember
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


def about(request):
    return render(request, 'myapp/about.html', {})


def contact(request):

    team_members = TeamMember.objects.all()

    context = {
        "team_members": team_members,
    }

    if request.method == "POST":
        name = request.POST.get("name")
        role = request.POST.get("role")
        age = request.POST.get("age")

        TeamMember.objects.create(
            name=name,
            role=role,
            age=age,
            is_active=False,            
        )

    return render(request, 'myapp/contact.html', context)


def join_us(request):

    if request.method == "POST":
        name = request.POST.get("name")
        role = request.POST.get("role")
        age = request.POST.get("age")

        TeamMember.objects.create(
            name=name,
            role=role,
            age=age,
            is_active=False,            
        )
    return render(request, 'myapp/join_us.html', {})