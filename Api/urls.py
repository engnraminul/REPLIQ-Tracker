from django.urls import path
from .views import api_home, api_create_company, api_company_dashboard, api_add_employee, api_add_device, api_checkout_device, api_checkout_device_return

urlpatterns = [
    path('home', api_home, name='api_home'),
    path('create_company', api_create_company, name='api_create_company'),
    path('company_dashboard', api_company_dashboard, name='api_company_dashboard'),
    path('add_employee/<int:company_id>/', api_add_employee, name='api_add_employee'),
    path('aadd_device/<int:company_id>/', api_add_device, name='api_add_device'),
    path('checkout_device/<int:company_id>/<int:device_id>/', api_checkout_device, name='api_checkout_device'),
    path('checkout_device_return/<int:company_id>/<int:device_id>/', api_checkout_device_return, name='api_checkout_device_return'),
    
]