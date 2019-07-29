from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
from app.models import appModel
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    serverTime=datetime.now()
    # return HttpResponse("<h1>Home Page</h1>")
    a = appModel.objects.all()
    return render(request,"home.html",{'a':a})
    # n1 = request.GET["num1"]
    # n2 = request.GET["num2"]
    # result = n1+n2
    # return render(request,"add.html",{"result":result})    
def about(request):
    # return HttpResponse("<h1>About Page</h1>")
    return render(request,"about.html")
def add(request):
    n1 = int(request.POST["num1"])
    n2 = int(request.POST["num2"])
    result = n1+n2
    return render(request,"add.html",{"result":result}) 
def register(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,"Account created for {}" .format(username))
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})