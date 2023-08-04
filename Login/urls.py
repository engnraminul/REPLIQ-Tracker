from django.contrib import admin
from django.urls import path, include
from Login import views


app_name = 'Login'
urlpatterns = [
    path("registration/", views.user_registration, name="user_registration"),
    path("", views.user_login, name="user_login"),
]