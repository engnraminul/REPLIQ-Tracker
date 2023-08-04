from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('user_login'))
            #return redirect('company_dashboard', company_id=user.employee.company.id)
    else:
        form = UserCreationForm()
    return render(request, 'login/registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
            #return redirect('company_dashboard', company_id=user.employee.company.id)
        else:
            context = {'error_message': 'Invalid credentials. Please try again.'}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login/login.html')
