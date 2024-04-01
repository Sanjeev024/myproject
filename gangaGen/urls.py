from django.contrib import admin
from django.urls import path, include
from gangaGen import views

urlpatterns = [
    path('', views.home, name='home'),
   path('database/', views.database, name='database'),
    path('user-login/', views.user_login, name='user_login'),
    path('logout/', views.logout_view, name="logout_view")
]
