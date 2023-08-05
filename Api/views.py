from django.shortcuts import render
from Tracker.models import Company, Employee, Device, DeviceLog
from Tracker.forms import CompanyForm, EmployeeForm, DeviceForm, CheckoutForm
from django.utils import timezone

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from Tracker.forms import CompanyForm, EmployeeForm, CheckoutForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
 


#Home API
@api_view(['GET'])
def api_home(request):
    content = render(request, "home.html")
    return Response({'content': content})

#URL- /api/home

@api_view(['POST'])
@login_required
def api_create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.data)
        if form.is_valid():
            company = form.save(user=request.user)
            return Response({'success': True, 'company_id': company.id})
        else:
            return Response({'success': False, 'errors': form.errors})

#URL- /api/create_company


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_company_dashboard(request):
    user = request.user
    company = get_object_or_404(Company, created_by=user)
    employees = company.employee_set.all()

    employees_data = []
    for employee in employees:
        checked_out_devices = DeviceLog.objects.filter(employee=employee)

        checked_out_devices_data = []
        for device_log in checked_out_devices:
            device_data = {
                'device_id': device_log.device.id,
                'device_name': device_log.device.name,
                'checkout_date': device_log.checkout_date,
                'checkin_date': device_log.checkin_date,
            }
            checked_out_devices_data.append(device_data)

        employee_data = {
            'employee_id': employee.id,
            'employee_name': employee.name,
            'checked_out_devices': checked_out_devices_data,
        }
        employees_data.append(employee_data)

    company_data = {
        'company_id': company.id,
        'company_name': company.name,
        'employees': employees_data,
    }
    return Response(company_data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_add_employee(request, company_id):
    company = get_object_or_404(Company, pk=company_id)

    if request.method == 'POST':
        form = EmployeeForm(request.data)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.company = company
            employee.save()
            return Response({'success': True})
        else:
            return Response({'success': False, 'errors': form.errors})
        




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_add_device(request, company_id):
    company = get_object_or_404(Company, pk=company_id)

    if request.method == 'POST':
        form = DeviceForm(request.data)
        if form.is_valid():
            device = form.save(commit=False)
            device.company = company
            device.save()
            return Response({'success': True})
        else:
            return Response({'success': False, 'errors': form.errors})



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_checkout_device(request, company_id, device_id):
    company = get_object_or_404(Company, pk=company_id)
    device = get_object_or_404(Device, pk=device_id, company=company)

    if request.method == 'POST':
        form = CheckoutForm(request.data, company=company)  # Pass company argument
        if form.is_valid():
            employee_name = form.cleaned_data['employee_name']
            employee = Employee.objects.get(name=employee_name, company=company)
            condition_on_checkout = form.cleaned_data['checkout_condition']
            
            device.status = 'unavailable'
            device.save()
            
            DeviceLog.objects.create(
                device=device,
                employee=employee,
                condition_on_checkout=condition_on_checkout,
                checkout_date=timezone.now(),
            )
            
            return Response({'success': True})
        else:
            return Response({'success': False, 'errors': form.errors})
        


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_checkout_device_return(request, company_id, device_id):
    device_log = DeviceLog.objects.filter(device_id=device_id, return_date__isnull=True).first()

    if device_log:
        device_log.return_date = timezone.now()
        device_log.save()
        
        device = device_log.device
        device.status = 'available'
        device.save()
    
        return Response({'success': True})
    else:
        return Response({'success': False})