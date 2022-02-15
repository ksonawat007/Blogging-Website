from django.shortcuts import render, redirect
from .forms import NewPostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='Login')
def Create(request):
    form = NewPostForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,"Post Added!")
        return redirect('Dashboard')
    
    context = {'form':form}
    return render(request,'blog/addPost.html',context)


def Read(request):
    pass

@login_required(login_url='Login')
def Update(request):
    pass

@login_required(login_url='Login')
def Delete(request):
    pass