from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Company, Employee, Device, DeviceLog
from .forms import CompanyForm, EmployeeForm, DeviceForm, CheckoutForm

def home(request):
    return render(request, "home.html")

@login_required
def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return HttpResponseRedirect(reverse('Tracker:home'))
            #return redirect('company_dashboard', company_id=request.user.employee.company.id)
    else:
        form = CompanyForm()
    return render(request, 'tracker/create_company.html', {'form': form})




@login_required
def company_dashboard(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    employees = company.employee_set.all()
    devices = company.device_set.all()
    context = {
        'company': company,
        'employees': employees,
        'devices': devices,
    }
    return render(request, 'tracker/company_dashboard.html', context)



@login_required
def company_dashboard(request):
    user = request.user
    company = Company.objects.get(created_by=user)
    employees = company.employee_set.all()
    devices = company.device_set.all()

    # Create a dictionary to store checked-out devices for each employee
    employees_data = []
    for employee in employees:
        checked_out_devices = DeviceLog.objects.filter(employee=employee)
        employee_data = {
            'employee': employee,
            'checked_out_devices': checked_out_devices,
        }
        employees_data.append(employee_data)

    context = {
        'company': company,
        'employees': employees,
        'devices': devices,
        'employees_data': employees_data,
    }
    return render(request, 'tracker/company_dashboard.html', context)


@login_required
def add_employee(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.company = company
            employee.save()
            return redirect('Tracker:company_dashboard')
    else:
        form = EmployeeForm()
    
    context = {
        'form': form,
        'company': company,
    }
    return render(request, 'tracker/add_employee.html', context)


#Add Device function views
@login_required
def add_device(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = form.save(commit=False)
            device.company = company
            device.save()
            return redirect('Tracker:company_dashboard')
    else:
        form = DeviceForm()
    
    context = {
        'form': form,
        'company': company,
    }
    return render(request, 'tracker/add_device.html', context)

@login_required
def checkout_device(request, company_id, device_id):
    company = get_object_or_404(Company, pk=company_id)
    device = get_object_or_404(Device, pk=device_id, company=company)
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST, company=company)  # Pass company argument
        if form.is_valid():
            employee_name = form.cleaned_data['employee_name']
            employee = Employee.objects.get(name=employee_name, company=company)
            condition_on_checkout = form.cleaned_data['checkout_condition']
            
            # Update device status and other details
            device.status = 'unavailable'
            device.save()
            
            # Create a checkout record or log for the employee
            DeviceLog.objects.create(
                device=device,
                employee=employee,
                condition_on_checkout=condition_on_checkout
            )
            
            return redirect('Tracker:company_dashboard')
    else:
        form = CheckoutForm(company=company)  # Pass company argument
    
    context = {
        'form': form,
        'company': company,
        'device': device,
    }
    return render(request, 'tracker/checkout_device.html', context)