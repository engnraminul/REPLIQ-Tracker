from django.contrib import admin
from django.urls import path, include

from Tracker import views

app_name = 'Tracker'
urlpatterns = [
    path("", views.home, name= "home"),
    path("Create-company/", views.create_company, name="create_company"),
    path("company-dashboard/", views.company_dashboard, name="company_dashboard"),
    path('company-dashboard/add-employee/<int:company_id>/', views.add_employee, name='add_employee'),
    path('company-dashboard/add-device/<int:company_id>/', views.add_device, name='add_device'),
    path('company-dashboard/<int:company_id>/checkout-device/<int:device_id>/', views.checkout_device, name='checkout_device'),
    
    
]