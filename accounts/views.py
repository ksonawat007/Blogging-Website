from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewUserForm, ProfileForm
from .models import NewUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from blog.models import Post

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = NewUserForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'User Created Successfully')
            return redirect('Login')

        context = {'form':form}
        return render(request,'accounts/register.html',context)


def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:    
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
    post_list = Post.objects.all()
    context = {'post_list':post_list}
    return render(request,'accounts/dashboard.html',context)

@login_required(login_url='Login')
def profile(request):
    profile = ProfileForm(request.POST or None)
    if profile.is_valid():
        profile.save()
        messages.success(request,'Profile Updated')
    context = {'profile':profile}
    return render(request,'accounts/profile.html',context)