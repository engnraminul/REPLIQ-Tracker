from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    return render(request, "home.html")


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Company
from .forms import CompanyForm

@login_required
def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save()
            return HttpResponseRedirect(reverse('Login:home', ))
            
            #return redirect('company_dashboard', company_id=company.id)
    else:
        form = CompanyForm()
    return render(request, 'tracker/create_company.html', {'form': form})