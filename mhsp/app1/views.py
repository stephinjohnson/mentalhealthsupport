from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



# Create your views here.

def HomePage(request):
    return render (request,"home.html")


# this is users signup 

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirm-password')

        if pass1!=pass2:
            return HttpResponse("your password is not same as confirm password")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
        return redirect('login')
    return render(request,"signup.html")  
        
# user
def LoginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("username or password is incorrect")
 

    
    return render (request,"login.html")

def logoutPage(request):
    logout(request)
    return redirect('login')


def ThreapistReg(request):
    return render (request,"thrpreg.html")

# oct 1 updations

def ThreapistReg(request):
    if request.method=='POST':
        fname=request.POST.get('first_name')
        lname=request.POST.get('last_name')
        licno=request.POST.get('license_number')
        tuname=request.POST.get('username')
        temail=request.POST.get('email')
        tpass1=request.POST.get('password')
        tpass2=request.POST.get('confirm-password')

        if tpass1!=tpass2:
            return HttpResponse("your password is not same as confirm password")
        else:
            my_user=User.objects.create_user(tuname,temail,tpass1)
            my_user.save()
        return redirect('login')
    return render(request,"thrpreg.html") 