from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.urls

from .models import Xusers

class xUserCreationForm(UserCreationForm):
    
    email = forms.EmailField(max_length=70)
    password1 = forms.CharField(max_length=70)
    password2 = forms.CharField(max_length=70)
    
    class Meta:
        model = Xusers
        fields = ('email','password1','password2')
        


    
    
        
    
    
