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

#therapist registration
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages



            
            
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
        return redirect('custom_admin_page')

def toggleUserStatus(request):
    if request.method == 'GET':
        user_id = request.GET.get('id')
        user = User.objects.get(id=user_id)
        user.is_active = not user.is_active  # Toggle the user's status
        user.save()
        return redirect('custom_admin_page')"""
    


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
        profile_picture =request.POST.GET('profile_picture')

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





#new updates

def ThreapistReg(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        role =  "THERAPIST"  # Assuming you have a field named 'role' in your form
        print(first_name)
        # user = User.objects.create_user(username=username, email=email, password=password, role=role)
        
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
        
            # user = User.objects.create_user(username=username, email=email, password=password, role=role)# NO NEED
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password,role=role)
            print(user)
       
        else:
            # Regular user registration logic
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password,role=role)
            user.save()
        return redirect('login')  
     
    return render(request, 'thrpreg.html')


#new updations on Therapist profile update


from django.shortcuts import render
from .models import User

def therapist_list(request):
    therapists = User.objects.filter(role=User.Role.THERAPIST)
    return render(request, 'therapist_list.html', {'therapists': therapists})




#new

from django.shortcuts import render, get_object_or_404
from .models import User

def update_therapist(request, therapist_id):
    therapist = get_object_or_404(User, id=therapist_id, role=User.Role.THERAPIST)
    
    if request.method == 'POST':
        therapist.phone = request.POST.get('phone')
        therapist.dob = request.POST.get('dob')
        therapist.location = request.POST.get('location')
        therapist.qualification = request.POST.get('qualification')
        therapist.description = request.POST.get('description')
        therapist.specialization = request.POST.get('specialization')

        # Handling profile_picture upload
        if 'profile_picture' in request.FILES:
            therapist.profile_picture = request.FILES['profile_picture']

        therapist.save()
        return render(request, 'success.html', {'message': 'Therapist details updated successfully!'})
    
    return render(request, 'therapist_update.html', {'therapist': therapist})


#testing
def Tdash(request):
    return render(request, 'Tdash.html')


from django.shortcuts import render
from .models import User

def Tdash(request):
    
    therapist = User.objects.get(id=request.user.id, role=User.Role.THERAPIST) #if any error is encouter please add  that Tdash on above
    print(f'Therapist ID: {therapist.id}') 
    return render(request, 'Tdash.html', {'therapist': therapist})


from django.shortcuts import render

def display_image(request):
    return render(request, 'image.html')

def displayTherapist(request):
    return render(request, 'therapistData.html')



# Fetch data from User table only the data of USER
from django.shortcuts import render
from .models import User

def user_list(request):
    users = User.objects.filter(role=User.Role.USER)
    return render(request, 'user_list.html', {'users': users})



from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

User = get_user_model()

def activate_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    return redirect('user_list')

def deactivate_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    return redirect('user_list')




from django.shortcuts import render
from .models import User

def therapist_list_new(request):
    therapists = User.objects.filter(role=User.Role.THERAPIST)
    return render(request, 'therapist_list_new.html', {'therapists': therapists})




from django.shortcuts import render, redirect
from .models import User

def approve_therapist(request, therapist_id):
    therapist = User.objects.get(id=therapist_id)
    therapist.is_approved = True
    therapist.save()
    return redirect('therapist_list_new')




#book appointment


# views.py

from django.shortcuts import render, redirect
from .models import User, Appointment
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required
def book_appointment(request, therapist_id):
    therapist = User.objects.get(pk=therapist_id, role=User.Role.THERAPIST)
    if request.method == 'POST':
        appointment_date = request.POST['appointment_date']
        appointment_date = datetime.strptime(appointment_date, '%Y-%m-%dT%H:%M')
        appointment = Appointment(user=request.user, therapist=therapist, appointment_date=appointment_date)
        appointment.save()
        return render(request, 'successappo.html', {'message': 'Appointment booked successfully!'})
    return render(request, 'book_appointment.html', {'therapist': therapist})


"""from django.shortcuts import render
from .models import User, Appointment 
from django.contrib.auth.decorators import login_required


@login_required
def therapist_appointments(request):
    if request.user.is_authenticated and request.user.is_therapist:
        pending_appointments = Appointment.objects.filter(therapist=request.user, is_approved=False)
        return render(request, 'therapist_appointments.html', {'appointments': pending_appointments})
    else:
        # Handle unauthorized access or redirect to login page
        pass"""

from django.shortcuts import render
from .models import User, Appointment 
from django.contrib.auth.decorators import login_required

@login_required
def therapist_appointments(request):
    if request.user.is_authenticated and request.user.role == User.Role.THERAPIST:
        pending_appointments = Appointment.objects.filter(therapist=request.user, is_approved=False)
        return render(request, 'therapist_appointments.html', {'appointments': pending_appointments})
    else:
        # Handle unauthorized access or redirect to login page
        pass


from django.shortcuts import get_object_or_404, redirect
from .models import Appointment

def approve_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    appointment.is_approved = True
    appointment.save()
    return redirect('successappo') 


def successappo(request):
    return render(request, 'successappo.html')




from django.shortcuts import render, redirect
from .models import User, Feedback

def therapist_list(request):
    therapists = User.objects.filter(role=User.Role.THERAPIST)

    context = {
        'therapists': therapists,
        'user': request.user,
    }

    return render(request, 'therapist_list.html', context)

def feedback_form(request, therapist_id):
    if request.method == 'POST':
        therapist = User.objects.get(id=therapist_id)
        user = request.user
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        feedback = Feedback.objects.create(therapist=therapist, user=user, rating=rating, comment=comment)
        # Optionally, you can redirect to the therapist profile page after submitting feedback
        return redirect('therapist_list')

    return render(request, 'feedback_form.html', {'therapist_id': therapist_id})

#

from django.shortcuts import render, get_object_or_404
from .models import User

def therapist_feedback(request, therapist_id):
    therapist = get_object_or_404(User, id=therapist_id, role=User.Role.THERAPIST)
    feedback = therapist.profile.therapist_feedback.all()

    context = {
        'therapist': therapist,
        'feedback': feedback,
    }

    return render(request, 'therapist_feedback.html', context)



# views.py
from django.shortcuts import render, redirect
from .forms import ArticleForm

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('article_list')  # Redirect to the list of articles
    else:
        form = ArticleForm()
    return render(request, 'add_article.html', {'form': form})



# views.py
from django.shortcuts import render
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})


from django.shortcuts import render, redirect



# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User, Schedule

@login_required
def schedule_appointment(request):
    if request.method == 'POST':
        therapist_id = request.POST.get('therapist_id')
        date_time = request.POST.get('date_time')
        duration = request.POST.get('duration')

        therapist = User.objects.get(id=therapist_id)
        user = request.user

        Schedule.objects.create(
            therapist=therapist,
            user=user,
            date_time=date_time,
            duration=duration
        )

        return redirect('appointment_list')

    therapists = User.objects.filter(role=User.Role.USER)
    return render(request, 'schedule_appointment.html', {'therapists': therapists})

@login_required
def appointment_list(request):
    user = request.user
    appointments = Schedule.objects.filter(user=user)
    return render(request, 'appointment_list.html', {'appointments': appointments})




from django.shortcuts import render, redirect
from .models import UserExperience
from django.contrib.auth.decorators import login_required

@login_required
def write_experience(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        # Create a new UserExperience instance and associate it with the current user
        UserExperience.objects.create(user=request.user, title=title, content=content)

        return redirect('experience_list')  # Redirect to the page displaying all experiences
    else:
        return render(request, 'write_experience.html')

@login_required
def experience_list(request):# this is only for one user
    experiences = UserExperience.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'experience_list.html', {'experiences': experiences})





from django.shortcuts import render, redirect, get_object_or_404
from .models import UserExperience

def edit_experience(request, experience_id):
    # Retrieve the experience to edit or return a 404 error if not found
    experience = get_object_or_404(UserExperience, id=experience_id)

    if request.method == 'POST':
        # Handle form submission for editing the experience
        title = request.POST.get('title')
        content = request.POST.get('content')

        # Update the experience with new data
        experience.title = title
        experience.content = content
        experience.save()

        return redirect('experience_list')  # Redirect to the page displaying all experiences
    else:
        return render(request, 'edit_experience.html', {'experience': experience})

def delete_experience(request, experience_id):
    # Retrieve the experience to delete or return a 404 error if not found
    experience = get_object_or_404(UserExperience, id=experience_id)

    if request.method == 'POST':
        # Handle form submission for deleting the experience
        experience.delete()

        return redirect('experience_list')  # Redirect to the page displaying all experiences
    else:
        return render(request, 'delete_experience.html', {'experience': experience})
    



def supportplatform(request):
    experiences = UserExperience.objects.all().order_by('-created_at')
    return render(request, 'supportplatform.html', {'experiences': experiences})



from django.shortcuts import get_object_or_404, redirect
from .models import Product


# views.py
from django.shortcuts import render, redirect
from .models import Product, Cart
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
# views.py


def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    user_cart, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        user_cart.quantity += 1
        user_cart.save()
    return redirect('add_to_cart_page')



# views.py
from django.shortcuts import render
from .models import Cart

def add_to_cart_page(request):
    user_carts = Cart.objects.filter(user=request.user)
    return render(request, 'add_to_cart_page.html', {'user_carts': user_carts})

# views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Cart

def add_to_cart_page(request):
    user_carts = Cart.objects.filter(user=request.user)
    return render(request, 'add_to_cart_page.html', {'user_carts': user_carts})

def update_cart_quantity(request, cart_id, action):
    if request.method == 'POST' and action in ['increment', 'decrement']:
        cart_item = Cart.objects.get(pk=cart_id, user=request.user)

        if action == 'increment':
            cart_item.quantity += 1
        elif action == 'decrement':
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
            else:
                cart_item.delete()

        cart_item.save()

        return JsonResponse({'success': True, 'new_quantity': cart_item.quantity})

    return JsonResponse({'success': False, 'error': 'Invalid request'})




from django.views.decorators.csrf import csrf_exempt
from razorpay import Client
from django.conf import settings


razorpay_api_key = settings.RAZORPAY_API_KEY
razorpay_secret_key = settings.RAZORPAY_API_SECRET

razorpay_client = Client(auth=(razorpay_api_key, razorpay_secret_key))


@csrf_exempt
def rentnxt(request):
    # Amount to be paid (in paisa), you can change this dynamically based on your logic
    amount = 1000

    # Create a Razorpay order (you need to implement this based on your logic)
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1',  # Auto-capture payment
    }

    # Create an order
    order = razorpay_client.order.create(data=order_data)

    context = {
        'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],
    }

    return render(request, 'payment.html', context)



# time slot

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TimeSlot

@login_required
def add_time_slot(request):
    if request.user.role != 'THERAPIST':
        return redirect('home')  # Redirect to the home page if the user is not a therapist

    if request.method == 'POST':
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        TimeSlot.objects.create(therapist=request.user, start_time=start_time, end_time=end_time)
        return redirect('new_view_time_slots')  # Redirect to the home page after adding the time slot

    return render(request, 'add_time_slot.html')

def view_time_slots(request):
    if request.user.role != 'USER':
        return redirect('home')  # Redirect to the home page if the user is not a regular user

    time_slots = TimeSlot.objects.all()
    return render(request, 'view_time_slots.html', {'time_slots': time_slots})


#new timeslotview

def new_view_time_slots(request):
    if request.user.role != 'THERAPIST':
        return redirect('home')  # Redirect to the home page if the user is not a therapist

    time_slots = TimeSlot.objects.filter(therapist=request.user)
    return render(request, 'new_view_time_slots.html', {'time_slots': time_slots})


@login_required
def edit_time_slot(request, time_slot_id):
    time_slot = get_object_or_404(TimeSlot, id=time_slot_id, therapist=request.user)

    if request.method == 'POST':
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        time_slot.start_time = start_time
        time_slot.end_time = end_time
        time_slot.save()
        return redirect('new_view_time_slots')  # Redirect to view_time_slots after editing the time slot

    return render(request, 'edit_time_slot.html', {'time_slot': time_slot})

@login_required
def delete_time_slot(request, time_slot_id):
    time_slot = get_object_or_404(TimeSlot, id=time_slot_id, therapist=request.user)

    if request.method == 'POST':
        time_slot.delete()
        return redirect('new_view_time_slots')  # Redirect to view_time_slots after deleting the time slot

    return render(request, 'delete_time_slot.html', {'time_slot': time_slot})