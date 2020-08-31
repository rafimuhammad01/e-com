from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer


class RegisterForm(UserCreationForm) :
    email = forms.EmailField()
    name = forms.CharField(max_length=50)
    gender = forms.ChoiceField(choices = ( 
    ("male", "Male"), 
    ("female", "Female")
    )) 

    class Meta :
        model = User
        fields = ['name','username', 'email','gender', 'password1','password2']

    def save(self, commit=True) :
        user = super(RegisterForm, self).save(commit=False)
        name = self.cleaned_data['name'].split()
        user.first_name = name[0]
        if len(name) == 2 :
            user.last_name = name[1]
        cust = Customer.objects.create(name=self.cleaned_data['name'])


        if commit:
            user.save()
            cust.save()


