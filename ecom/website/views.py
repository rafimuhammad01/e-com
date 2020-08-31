from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from django.contrib.auth.models import User
from .models import Customer


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
            login(request, authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1']))
            
            return redirect('emailVerification')

    context = {'form' : form}
    return render(request, 'website/register.html', context)

def emailVerification(request) :
    if request.user.is_authenticated :
        user = Customer.objects.get(username=request.user.get_username())
        print(user.email_verification_key)
        if user.email_verification :
            return render(request, 'website/emailConfirmation.html')
        else : 
            subject = 'Email Verification'
            message = 'Please go to this link \nwww.localhost:8000/email-verification/' + user.email_verification_key
            from_mail = settings.EMAIL_HOST_USER
            to_list = [request.user.email, settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_mail, to_list, fail_silently=False)
            return render(request, 'website/emailVerification.html')


    return redirect('loginPage')

def confirmedEmail(request, name) :
    user = Customer.objects.get(username=request.user.get_username())
    if user.email_verification_key == name :
        user.email_verification = True
        user.save()
    return redirect("emailVerification")

