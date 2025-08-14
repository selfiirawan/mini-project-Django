"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from myapp.views import home, my_page

urlpatterns = [
    # admin/ - is an admin panel, provided by django
    # admin.site.urls - 
    path("admin/", admin.site.urls),

    # 'home/' - is the url of our new page
    # home - is the View function that will serve our new page
    # can access the new page via the link: 'http://127.0.0.1:8000/home'
    path('home/', home),
    path('my-page/', my_page)
]
