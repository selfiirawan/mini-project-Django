
from django.shortcuts import render, redirect
from datetime import datetime
from myapp.models import Movie, Food, TeamMember, Product
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

    context = {
        "product": product,
    }

    return render(request, 'myapp/edit_product.html', context)