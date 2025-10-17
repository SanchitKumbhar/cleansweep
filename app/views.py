from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate,get_user_model
from django.http import JsonResponse,HttpResponse
from .models  import *
User = get_user_model()
# Create your views here.
def signup_user(request):
    username = request.POST.get("username")
    password=request.POST.get("password")

    user=User.objects.create_user(username=username,password=password)

    login(request,user)
    return redirect("/client") 

    
def authenticatepage(request):
    return render(request,"login.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Check if the user is an admin
            if user.is_superuser:
                return redirect("/admin-page")
            else:
                return redirect("/client")
        else:
            return HttpResponse("Invalid username or password.")
    
    return render(request, "login.html")

def client(request):
    reports = Report.objects.filter(user=request.user)
    return render(request,"client.html",{"reports" : reports})

def adminpage(request):
    if request.user.is_superuser:
        reports = Report.objects.all()
        print(reports)
        return render(request,"admin.html",{"reports":reports})
    else:
        return HttpResponse("Permission Denied!!!")

def reportpage(request):
    if request.method == "POST":
        file = request.FILES["file"]
        name=request.POST.get("name")
        mobile=request.POST.get("mobile")
        description=request.POST.get("description")
        
        print(file)
    
        Report.objects.create(picture=file,name=name,mobile=mobile,description=description,user=request.user)
    return render(request,"report.html")

def logoutuser(request):
    logout(request)
    return redirect("/authenticate")

def feedback(request):
    return render(request,"feedback.html")

def track(request):
    return render(request,"track.html")

