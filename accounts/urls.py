from django.urls import path
from django.shortcuts import render
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.registeruser, name="register"),
    path('login/', views.loginuser, name="login"),
    path('logout/', views.logoutuser, name="logout"),
    path('edit/<int:pk>/', views.edituser, name="edituser"),

    
    
]