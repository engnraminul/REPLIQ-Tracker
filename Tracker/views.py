from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Company
from .forms import CompanyForm, EmployeeForm

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
    #employees = company.employee_set.all()
    #devices = company.device_set.all()
    context = {
        'company': company,
        #'employees': employees,
        #'devices': devices,
    }
    return render(request, 'tracker/company_dashboard.html', context)