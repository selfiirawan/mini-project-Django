
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from myapp.models import Movie, Food, TeamMember, Product, Studio
from myapp.forms import StudioForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
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
        "movies": movies,
        "foods": foods,
    }
    
    # 3 (go to home.html) - use data on html

    return render(request, 'myapp/home.html', context)


def about(request):
    return render(request, 'myapp/about.html', {})


def contact(request):

    return render(request, 'myapp/contact.html', {})


@login_required
def join_us(request):

    team_members = TeamMember.objects.all()

    context = {
        "team_members": team_members,
    }

    if request.method == "POST":
        name = request.POST.get("name")
        role = request.POST.get("role")
        age = request.POST.get("age")

        print(f"\nName: {name}")
        print(f"Role: {role}")
        print(f"Age: {age}\n")

        TeamMember.objects.create(
            name=name,
            role=role,
            age=age,
            is_active=False,            
        )

    return render(request, 'myapp/join_us.html', context)


@login_required
def create_product(request):

    products = Product.objects.all()
    count_products = products.count()

    context = {
        "products": products,
        "count_products": count_products,
    }

    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.POST.get("image")

        print(f"\nName: {name}")
        print(f"Price: RM{price}")
        print(f"Description: {description}\n")

        Product.objects.create(
            name=name,
            price=price,
            description=description,
            image=image,
        )

        #return redirect("home")
        return redirect("create_product")

    return render(request, 'myapp/create_product.html', context)


def delete_all_products(request):

    if request.method == "POST":
        products = Product.objects.all()

        products.delete()

    return redirect("home")


def delete_product(request, product_id):

    if request.method == "POST":
        product = Product.objects.get(id=product_id)

        print(f"\nDeleting product: {product.name} ({product.id})\n")
        product.delete()

    return redirect("create_product")


def edit_product(request, product_id):
    
    product = Product.objects.get(id=product_id)

    # after user clicks the "Save" button
    if request.method == "POST":
        
        # get the updated data from the form 
        image = request.POST.get("image")
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")

        # update the model 
        product.image = image
        product.name = name
        product.price = price
        product.description = description

        product.save()

        return redirect("create_product")

    context = {
        "product": product,
    }

    return render(request, 'myapp/edit_product.html', context)


def user_login(request):

    if request.method == "POST":
        print("\nUser tried to login. \n")

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        print(f"User: {user}\n")

        if user:
            login(request, user)

            return redirect("home")
        
        else:
            print("\nInvalid user / password. Please try again!\n")
            messages.error(request, "Invalid username or password! Please try again.")

    return render(request, 'myapp/login.html', {})


def user_logout(request):

    print("\nUser logged out.\n")

    logout(request)

    return redirect("home")


def register_user(request):

    if request.method == "POST":
        print("\nRegistering new user...")

        # when user clicks Submit
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        print(f"\nUsername: {username}")
        print(f"Password: {password}")
        print(f"Confirm Password: {confirm_password}\n")


        ######## BASIC VALIDATION ########

        # check if the password matches 
        if password != confirm_password:
            print("\nPassword doesn't match!\n")
            messages.error(request, "Passwords do not match!")
            return render(request, 'myapp/register.html', {})
        
        # return True / False 
            # True - if user exist 
            # False - if user doesn't exist 
        is_user_exist = User.objects.filter(username=username).exists()

        # check if user already exist
        if is_user_exist == True:
            print("\nUser already exist! Please choose another username.\n")
            messages.error(request, "User already exists! Please choose another username.")
            return render(request, 'myapp/register.html', {})
        
        ##################################

        # create the new user and redirect to login page 
        user = User.objects.create_user(
            username=username,
            password=password,
        )

        return redirect("user_login")

    return render(request, 'myapp/register.html', {})


def studio_list(request):
    
    city = request.GET.get("city")

    studios = Studio.objects.all()

    if request.method == "POST":
        form = StudioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("studio_list")
    
    else:
        form = StudioForm()

    if city:
        studios = studios.filter(city__iexact=city)

    context = {
        "studios": studios,
        "form": form,
        "selected_city": city,
    }

    return render(request, 'myapp/studios.html', context)


def studio_detail(request, studio_id):
    studio = get_object_or_404(Studio, id=studio_id)

    context = {
        "studio": studio,
    }

    return render(request, 'myapp/studio_detail.html', context)