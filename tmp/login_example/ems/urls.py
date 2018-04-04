"""sb_ems URL Configuration

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

from .views import list_products, create_product, update_product, delete_product

urlpatterns = [
    path('', list_products, name='list_products'),
    path('new', create_product, name='create_product'),
    path('update/<int:id>/', update_product, name='update_product'),
    path('deletE/<int:id>/', delete_product, name='delete_product'),
]
