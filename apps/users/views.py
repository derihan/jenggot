from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login,authenticate
from django.conf import settings
from .forms import xUserCreationForm


# Create your views here.


def login_form(request):
    # _form = xUserCreationForm()
    context = {'private_url': settings.BASE_URL + "auth/check",'judul':'Login'}
    return render(request, 'akun/login.html',context)


def registerForm(request):
    
    context = {'private_url': settings.BASE_URL +
               "auth/save-account/",'judul':'Register'}
    return render(request, 'akun/signup.html', context)


def save_action(request):
    context = []
    if request.POST:
        form = xUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password2 = form.cleaned_data.get('password2')
            # users = authenticate(email=email, password=password2)
            # login(request)
            status = 1
            msg = "regster sukses"
            # print('sukses')
        else:
            status = 0
            msg = [(k, v[0]) for k, v in form.errors.items()]
    return JsonResponse({'status': status, 'msg':msg})
