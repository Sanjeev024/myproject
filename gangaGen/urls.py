from django.contrib import admin
from django.urls import path, include
from gangaGen import views

urlpatterns = [
    path('', views.home, name='home'),
    path('database', views.database, name='database')
]
