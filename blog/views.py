from django.shortcuts import render, redirect
from .forms import NewPostForm
from django.contrib import messages

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

def Update(request):
    pass

def Delete(request):
    pass