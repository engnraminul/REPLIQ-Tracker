from django.contrib import admin
from django.urls import path, include

from Tracker import views

app_name = 'Tracker'
urlpatterns = [
    path("", views.home, name= "home"),
    path("Create-company/", views.create_company, name="create-company"),
    
]