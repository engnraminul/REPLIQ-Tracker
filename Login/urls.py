from django.contrib import admin
from django.urls import path, include
from Login import views


app_name = 'Login'
urlpatterns = [
    path("", views.user_login, name="user_login"),
    path("registration/", views.user_registration, name="user_registration"),
    path("logout/", views.user_logout, name="user_logout"),
    
]