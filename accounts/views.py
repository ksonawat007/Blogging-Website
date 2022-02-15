from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewUserForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    form = NewUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'User Created Successfully')
        return redirect('Login')

    context = {'form':form}
    return render(request,'accounts/register.html',context)


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('Dashboard')
        else:
            messages.info(request,"Incorrect username/password")
            
    return render(request,'accounts/login.html',{})

@login_required(login_url='Login')
def Logout(request):
    logout(request)
    return redirect('Login')

@login_required(login_url='Login')
def dashboard(request):
    return render(request,'accounts/dashboard.html',{})

@login_required(login_url='Login')
def profile(request):
    profile = ProfileForm(request.POST or None)
    if profile.is_valid():
        profile.save()
        messages.success(request,'Profile Updated')
    context = {'profile':profile}
    return render(request,'accounts/profile.html',context)