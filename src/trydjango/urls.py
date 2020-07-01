"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from pages.views import index, checkdiabetes, symptom, Diet,aitester, Home, product_create_view,diabetes_form,home_view,diabetes_formdetail, aitestersecond
from products.views import product_detail_view, product_create_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('index/',index,name='index'),
    path('checkdiabetes/',checkdiabetes,name='checkdiabetes'),
    path('Diet/',Diet,name='Diet'),
    path('aitester/', aitester, name='aitester'),
    path('symptom/', symptom, name='symptom'),
    path('Home/',Home,name='Home'),
    path('create/', product_create_view),
    # path('diabetesform/',diabetes_form),
    path('homeview/',home_view,name='home'),
    path('product/', product_detail_view),

    path('formdetail/', diabetes_formdetail),
    path('productdatabase/', product_create_view),
    path('userdata/', diabetes_form),
    path('aitestersecond/', aitestersecond),

]
