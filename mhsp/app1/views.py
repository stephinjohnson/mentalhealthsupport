from django.shortcuts import render,redirect,HttpResponse
from .models import User
from django.contrib.auth import authenticate ,login as auth_login,logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache



# Create your views here.
@login_required
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
                      if User.objects.get(email=email):   #email id goes to database...
                             messages.warning(request,"email ID is already taken")
                             return render(request,'signup.html')
            except Exception as identifiers:
                      pass
            
           # print(first_name,last_name,username,email,password)
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password,role='USER')
              #make the user inactive  user.is_active=False
            user.save()
            return redirect('login')
   return render(request,'signup.html')

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

def signupnew(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        role = request.POST['role']  # Assuming you have a field named 'role' in your form

        user = User.objects.create_user(username=username, email=email, password=password, role=role, phone_number=phone_number, dob=dob, location=location)
        
        # Check if the user is a therapist and create a therapist instance
        
        
        
        if password != confirm_password:
            messages.warning(request, "Password is not matching")
            return render(request, 'thrpreg.html')
        
        try:
            if User.objects.get(username=username):
                messages.warning(request, "Username is already taken")
                return render(request, 'thrpreg.html')
            if User.objects.get(email=email):
                messages.warning(request, "Email ID is already taken")
                return render(request, 'thrpreg.html')
        except User.DoesNotExist:
            pass

        if role == 'THERAPIST':
            # Logic specific to therapist registration can go here
            # For example, you can create a Therapist model and save additional therapist-related information
            pass
        
            user = User.objects.create_user(username=username, email=email, password=password)# NO NEED
        
        if is_therapist:
            user.is_staff = True  # Set is_staff to True for therapists
            user.save()   # NO NEED
        else:
            # Regular user registration logic
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password,role='THERAPIST')
            user.save()
            return redirect('login')
        
        
    
    return render(request, 'thrpreg.html')

            
# user
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login as auth_login

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        # Use the model class to query the database
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            if user.role == 'USER':
                request.session['username'] = username
                messages.success(request, "Login Success!!!")
                return redirect('home')
            elif user.role == 'THERAPIST':
                request.session['username'] = username
                messages.success(request, "Login Success!!!")
                return redirect('Tdash')
            elif user.role == 'ADMIN':
                auth_login(request, user)  # You had a login() call here, which was causing the error
                user_profiles = User.objects.exclude(id=user.id)
                # Pass the data to the template
                context = {'user_profiles': user_profiles}
                return render(request, 'demo.html', context)
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    
    return render(request, 'login.html')


def logoutPage(request):
    logout(request)
    return redirect('login')

def adminpage(request):
    return render (request,"demo.html")

# oct 1 updations TherapHome



def TherapHome(request):
    return render(request,"demo.html")

#oct5 edit.....
def EditProfile(request):
     return render(request,"edit.html")

def custom_admin_page(request):
    # Query all User objects (using the custom user model) from the database
    # Render the HTML template
    return render(request, 'demo.html')

"""def removeUser(request):
    if request.method == 'GET':
        user = User.objects.get(id=request.GET['id'])
        user.delete()
        return redirect('custom_admin_page')
    
#deactivate user

def deactivateUser(request):
    if request.method == 'GET':
        user = User.objects.get(id=request.GET['id'])
        user.is_active = False
        user.save()
        return redirect('custom_admin_page')
    
#activate user

def activateUser(request):
    if request.method == 'GET':
        user = User.objects.get(id=request.GET['id'])
        user.is_active = True
        user.save()
        return redirect('custom_admin_page')"""

def toggleUserStatus(request):
    if request.method == 'GET':
        user_id = request.GET.get('id')
        user = User.objects.get(id=user_id)
        user.is_active = not user.is_active  # Toggle the user's status
        user.save()
        return redirect('custom_admin_page')
    


from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User

@login_required
def update_profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        dob = request.POST.get('dob')
        location = request.POST.get('location')

        # Parse and format the date
        try:
            dob_date = datetime.strptime(dob, '%Y-%m-%d').date()
        except ValueError:
            # Handle invalid date format here
            return render(request, 'update.html', {'error': 'Invalid date format. Please use YYYY-MM-DD.'})

        # Get the user object
        user = request.user

        # Update user profile fields
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.phone_number = phone_number
        user.dob = dob_date
        user.location = location
        user.save()

        return redirect('/home')  # Redirect to the user's profile page after successful update

    return render(request, 'update.html')



def product(request):
     return render(request,"merchand.html")


from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to a page displaying the list of products
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})



from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list page
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')  # Redirect to the product list page
    return render(request, 'delete_product.html', {'product': product})


def ProductForUser(request):
    return render(request, 'listforuser.html')# not necessaryy


from django.shortcuts import render
from .models import Product

def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'product_list_user.html', {'products': products})

from django.shortcuts import get_object_or_404, redirect
from .models import Product

def buy_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    return redirect('product_list_user')

from django.shortcuts import get_object_or_404, redirect
from .models import Product

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    return redirect('product_list_user')


def ThreapistReg(request): #no use
    return render(request,"thrpreg.html") 

def TherapistHome(request): #no use
    return render(request,"Tdash.html") 


from django.contrib.auth.models import User  # this is fo separate user and therapist

def get_users():
    return User.objects.filter(is_staff=False)

def get_therapists():
    return User.objects.filter(is_staff=True)






