from django.shortcuts import render
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from employee.models import Employee
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def login_user(request):
    if request.method == "POST":
        id = request.POST["id"]
        password = request.POST["password"]
        user = authenticate(request,username=id,password=password)
        if user is not None:
            login(request , user)
            return redirect("/ems/dashboard")
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("/")

    return render(request,"employee/Login.html")


def logout_user(request):
    logout(request)
    return redirect("/")


def signup(request):
    if request.method == "POST":
        id = request.POST["id"]
        password = request.POST["password"]
        cnfpass = request.POST["cnfpass"]
        
        if password != cnfpass:
            messages.info(request, "Password Doesn't Match")
            return redirect("/signup")

        # Check if employee exists
        if not Employee.objects.filter(eID=id).exists():
            messages.info(request, "Invalid Employee")
            return redirect("/signup")

        # Check if user already exists
        if User.objects.filter(username=id).exists():
            messages.info(request, "Employee Already Registered")
            return redirect("/signup")

        # Create new user
        user = User.objects.create_user(username=id, password=password)
        user.save()
        messages.success(request, "Registered Successfully")
        return redirect("/login")  # ✅ Redirect to login page after signup

    return render(request, "employee/signup.html")