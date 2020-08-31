from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

# Create your views here.

def landing_page(request) :
    return HttpResponse("this is landing page")

def loginPage(request) :
    return render(request,'website/login.html')

def registerPage(request) :
    form = RegisterForm()
    

    if request.method == "POST" :
        form = RegisterForm(request.POST)
        if form.is_valid() :
            form.save()
        

    context = {'form' : form}
    return render(request, 'website/register.html', context)
