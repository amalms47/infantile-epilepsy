from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            messages.error(request, 'Incorrect credentials')
    return render(request,"index.html", {})

@login_required
def dashboard(request):
    context={}
    context['user']=request.user
    return render(request,"dashboard.html",context)


@login_required
def baselinedata(request):
    context={}
    context['user']=request.user
    return render(request,"baselinedata.html",context)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def error_404(request):
    context={}
    return render(request,"404.html",context)