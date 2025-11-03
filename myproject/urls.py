"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import (
    home, 
    contact, 
    about, 
    join_us,
    create_product,
    delete_all_products,
    delete_product,
    edit_product,
    user_login,
    user_logout,
)

urlpatterns = [
    # admin/ : is an admin panel, that django provides us.
    path('admin/', admin.site.urls),

    path('', home, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('join-us/', join_us, name="join_us"),
    path('create-product/', create_product, name="create_product"),
    path('delete-all-products/', delete_all_products, name="delete_all_products"),
    path('delete-product/<product_id>/', delete_product, name="delete_product"),
    path('edit-product/<product_id>/', edit_product, name="edit_product"),
    path('login/', user_login, name="user_login"),
    path('logout/', user_logout, name="user_logout"),
]