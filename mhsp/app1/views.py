from django.shortcuts import render,redirect,HttpResponse
from .models import User 

from django.contrib.auth import authenticate ,login as auth_login,logout
from django.contrib import messages



# Create your views here.

def home(request):
    return render (request,"home.html")


# this is users signup 

"""def SignupPage(request):
      if request.method=='POST':
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        nuname=request.POST.get('username')
        nemail=request.POST.get('email')
        npass1=request.POST.get('password')
        npass2=request.POST.get('confirm-password')

        #if npass1!=npass2:
        #    return HttpResponse("your password is not same as confirm password")
        if UserProfile.objects.filter(username=nuname).exists() or TherapistProfile.objects.filter(username=tuname).exists():
        #else:
         my_user=UserProfile.objects.create_user(nuname,nemail,npass1)
         my_user.save()
         return redirect('login')
      return render(request,"signup.html") """

def signup(request):
   if request.method=="POST":
            first_name=request.POST['firstname']
            last_name=request.POST['lastname']
            email=request.POST['email']
            username=request.POST['username']
            password=request.POST['password']
            confirm_password=request.POST['confirm-password']
            if password!=confirm_password:
                    messages.warning(request,"password is not matching")
                    return render(request,'signup.html')
            try:
                      if User.objects.get(username=username):
                             messages.warning(request,"Username is already taken")
                             return render(request,'signup.html')
            except Exception as identifiers:
                      pass
            print(first_name,last_name,username,email,password)
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password,role='USER')
              #make the user inactive  user.is_active=False
            user.save()
            return redirect('login')
   return render(request,'signup.html')
            
# user
def login(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
        
        # Use the model class to query the database
        user = authenticate(request,username=username, password=password)
        
        if user is not None:
            auth_login(request,user)
            if user.role=='USER':
               messages.success(request,"Login Success!!!")
               return redirect('home')
            elif user.role=='THERAPIST':
               messages.success(request,"Login Success!!!")
               return HttpResponse("seller login")
            elif user.role=='ADMIN':
               messages.success(request,"Login Success!!!")
               return HttpResponse("Admin login ")
                          
        else:
            messages.error(request,"Some thing went wrong")
            return redirect('login')
    return render(request,'login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')


def ThreapistReg(request):
    return render (request,"thrpreg.html")

# oct 1 updations

def ThreapistReg(request):
    return render(request,"thrpreg.html") 