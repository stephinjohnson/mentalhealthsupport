from django.shortcuts import render,redirect,HttpResponse
from .models import User
from django.contrib.auth import authenticate ,login as auth_login,logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache



# Create your views here.
from django.shortcuts import render
from .models import Appointment

@login_required
def home(request):
    # Fetch the user's appointments
    user_appointments = Appointment.objects.filter(user=request.user)
    return render(request, "home.html", {'user_appointments': user_appointments})



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

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

@login_required
def update_profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        dob = request.POST.get('dob')
        location = request.POST.get('location')
        profile_picture = request.FILES.get('profile_picture')  # Use request.FILES to get the file data

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

        if profile_picture:
            # Save the uploaded profile picture to the user's profile
            file_name = f"profile_pictures/{user.username}_{profile_picture.name}"
            user.profile_picture.save(file_name, ContentFile(profile_picture.read()))

        user.save()

        return redirect('/home')  # Redirect to the user's profile page after a successful update

    return render(request, 'update.html')


def product(request):
     return render(request,"merchand.html")


from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Include request.FILES for handling file uploads
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
    try:
        therapist = User.objects.get(id=request.user.id, role=User.Role.THERAPIST)
        appointments = Appointment.objects.filter(therapist=therapist, status='PENDING')
        print(f'Therapist ID: {therapist.id}')
        return render(request, 'Tdash.html', {'therapist': therapist, 'appointments': appointments})
    except User.DoesNotExist:
        # Handle the case where the user is not found or is not a therapist
        return redirect('home')  # Redirect to the home page or handle appropriately


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

# from django.shortcuts import render, redirect
# from .models import User, Appointment
# from django.contrib.auth.decorators import login_required
# from datetime import datetime

# @login_required
# def book_appointment(request, therapist_id):
#     therapist = User.objects.get(pk=therapist_id, role=User.Role.THERAPIST)
#     if request.method == 'POST':
#         appointment_date = request.POST['appointment_date']
#         appointment_date = datetime.strptime(appointment_date, '%Y-%m-%dT%H:%M')
#         appointment = Appointment(user=request.user, therapist=therapist, appointment_date=appointment_date)
#         appointment.save()
#         return render(request, 'successappo.html', {'message': 'Appointment booked successfully!'})
#     return render(request, 'book_appointment.html', {'therapist': therapist})


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


#appointment old one 
#views.py
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .models import User, Schedule

# @login_required
# def schedule_appointment(request):
#     if request.method == 'POST':
#         therapist_id = request.POST.get('therapist_id')
#         date_time = request.POST.get('date_time')
#         duration = request.POST.get('duration')

#         therapist = User.objects.get(id=therapist_id)
#         user = request.user

#         Schedule.objects.create(
#             therapist=therapist,
#             user=user,
#             date_time=date_time,
#             duration=duration
#         )

#         return redirect('appointment_list')

#     therapists = User.objects.filter(role=User.Role.USER)
#     return render(request, 'schedule_appointment.html', {'therapists': therapists})

# @login_required
# def appointment_list(request):
#     user = request.user
#     appointments = Schedule.objects.filter(user=user)
#     return render(request, 'appointment_list.html', {'appointments': appointments})




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

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed, JsonResponse
from .models import Product, Cart

def add_to_cart(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return HttpResponseNotAllowed("Product does not exist.")

    user_cart, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        user_cart.quantity += 1
        user_cart.save()

    return redirect('add_to_cart_page')

def add_to_cart_page(request):
    user_carts = Cart.objects.filter(user=request.user)
    return render(request, 'add_to_cart_page.html', {'user_carts': user_carts})

from django.db.models import F

@login_required
def update_cart_quantity(request, cart_id, action):
    if request.method == 'POST' and action in ['increment', 'decrement']:
        cart_item = get_object_or_404(Cart, pk=cart_id, user=request.user)

        if action == 'increment':
            cart_item.quantity = F('quantity') + 1
        elif action == 'decrement':
            if cart_item.quantity > 1:
                cart_item.quantity = F('quantity') - 1
            else:
                cart_item.delete()

        cart_item.save()

        # Update the total price of the cart item
        cart_item.refresh_from_db()
        total_price = cart_item.quantity * cart_item.product.price
        cart_item.total_price = total_price
        cart_item.save()

        return JsonResponse({'success': True, 'new_quantity': cart_item.quantity, 'total_price': total_price})

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
from datetime import datetime, date
from django.shortcuts import render, redirect
from .models import TimeSlot

@login_required
def add_time_slot(request):
    if request.user.role != 'THERAPIST':
        return redirect('home')  # Redirect to the home page if the user is not a therapist

    default_time_slots = ["8-9", "9-10"]  # Set your default time slots here as a list

    if request.method == 'POST':
        session_type = request.POST.get('session_type')
        selected_time_slots = request.POST.getlist('time_slots[]')  # Use getlist to get multiple selected time slots
        
        # Default to today's date if 'start_date' is not provided
        start_date = request.POST.get('start_date', date.today())

        for time_slot in selected_time_slots:
            # Construct start_time and end_time directly from the selected time_slot
            start_time_str = f"{start_date} {time_slot.split('-')[0]}:00"
            end_time_str = f"{start_date} {time_slot.split('-')[1]}:00"

            # Convert the start_time and end_time strings to datetime objects
            start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
            end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")

            # Use start_time and end_time directly in the TimeSlot.objects.create() call
            TimeSlot.objects.create(
                therapist=request.user,
                session_type=session_type,
                time_slot=time_slot,
                start_time=start_time,
                end_time=end_time
            )

        return redirect('new_view_time_slots')  # Redirect to the home page after adding the time slots

    context = {
        'time_slots': TimeSlot.TIME_SLOTS,
        'default_time_slots': default_time_slots,
    }

    return render(request, 'add_time_slot.html', context)

# views.py
from django.shortcuts import render
from .models import TimeSlot

def view_time_slots(request):
    time_slots = TimeSlot.objects.filter(is_booked=False)

    return render(request, 'view_time_slots.html', {'time_slots': time_slots})


# #new timeslotview

from django.shortcuts import render, redirect
from .models import TimeSlot

@login_required
def new_view_time_slots(request):
    if request.user.role != 'THERAPIST':
        return redirect('home')  # Redirect to the home page if the user is not a therapist

    time_slots = TimeSlot.objects.filter(therapist=request.user)

    selected_time_slot_id = request.GET.get('selected_time_slot_id')  # Get the selected time slot ID from the query parameters
    selected_time_slot = None

    if selected_time_slot_id:
        try:
            selected_time_slot = TimeSlot.objects.get(id=selected_time_slot_id, therapist=request.user)
        except TimeSlot.DoesNotExist:
            selected_time_slot = None

    return render(request, 'new_view_time_slots.html', {'time_slots': time_slots, 'selected_time_slot': selected_time_slot})



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






#community forum
# views.py
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Thread, Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ThreadListView(View):
    def get(self, request):
        threads = Thread.objects.all()
        return render(request, 'thread_list.html', {'threads': threads})

class ThreadDetailView(View):
    def get(self, request, thread_id):
        thread = get_object_or_404(Thread, pk=thread_id)
        posts = Post.objects.filter(thread=thread)
        return render(request, 'thread_detail.html', {'thread': thread, 'posts': posts})

@method_decorator(login_required, name='dispatch')
class CreateThreadView(View):
    def get(self, request):
        return render(request, 'create_thread.html')

    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        creator = request.user
        thread = Thread.objects.create(title=title, content=content, creator=creator)
        return render(request, 'thread_detail.html', {'thread': thread, 'posts': []})

@method_decorator(login_required, name='dispatch')
class CreatePostView(View):
    def get(self, request, thread_id):
        thread = get_object_or_404(Thread, pk=thread_id)
        return render(request, 'create_post.html', {'thread': thread})

    def post(self, request, thread_id):
        content = request.POST.get('content')
        author = request.user
        thread = get_object_or_404(Thread, pk=thread_id)
        post = Post.objects.create(thread=thread, content=content, author=author)
        return render(request, 'thread_detail.html', {'thread': thread, 'posts': [post]})


# app1/views.py
from django.shortcuts import render
from django.views import View
from .models import Thread

class UserThreadListView(View):
    def get(self, request, username):
        threads = Thread.objects.filter(creator__username=username)
        return render(request, 'thread_list_user.html', {'threads': threads, 'username': username})





#Feb 23 update

from django.shortcuts import render, redirect
from .models import TimeSlot, Appointment
from django.contrib import messages

def book_appointment(request, time_slot_id):
    if request.user.role != 'USER':
        return redirect('home')  # Redirect to the home page if the user is not a regular user

    time_slot = TimeSlot.objects.get(pk=time_slot_id)

    # Check if the user already has a pending appointment with the same therapist and time slot
    existing_appointment = Appointment.objects.filter(
        user=request.user,
        therapist=time_slot.therapist,
        time_slot=time_slot,
        status='PENDING'
    ).exists()

    if not existing_appointment:
        # Create a new pending appointment
        Appointment.objects.create(
            user=request.user,
            therapist=time_slot.therapist,
            time_slot=time_slot,
            status='PENDING',
            status_change_notification=True
        )

        # Mark the time slot as booked
        time_slot.is_booked = True
        time_slot.save()

        messages.success(request, f"Appointment request sent to {time_slot.therapist.username}")

        # Redirect to the 'view_time_slots' page
        return redirect('new_paymenttok')
    else:
        messages.warning(request, f"You already have a pending appointment request with {time_slot.therapist.username}")

    return redirect('view_time_slots')





# views.py
from django.shortcuts import render, redirect
from .models import TimeSlot, Appointment
from django.contrib import messages

def therapist_appointments(request):
    if request.user.role != 'THERAPIST':
        return redirect('home')  # Redirect to the home page if the user is not a therapist

    appointments = Appointment.objects.filter(therapist=request.user, status='PENDING')
    return render(request, 'therapist_appointments.html', {'appointments': appointments})

def approve_appointment(request, appointment_id):
    if request.user.role != 'THERAPIST':
        return redirect('home')  # Redirect to the home page if the user is not a therapist

    appointment = Appointment.objects.get(pk=appointment_id)

    # Check if the appointment belongs to the therapist
    if appointment.therapist != request.user:
        return redirect('home')  # Redirect to the home page if the therapist does not own the appointment

    appointment.status = 'APPROVED'
    appointment.save()

    messages.success(request, f"Appointment with {appointment.user.username} approved successfully")
    return redirect('therapist_appointments')

#views.py
from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings  # Import settings to access email configuration
from django.shortcuts import get_object_or_404, redirect
from .models import Appointment

def therapist_approve_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, therapist=request.user, status='PENDING')

    if request.method == 'POST':
        if 'approve' in request.POST:
            appointment.status = 'APPROVED'
            appointment.status_change_notification = True
            appointment.save()

            # Send approval notification email to the user
            send_approval_notification(appointment)

            return redirect('therapist_appointments')

        elif 'reject' in request.POST:
            appointment.status = 'REJECTED'
            appointment.status_change_notification = True
            appointment.save()
            send_approval_notification(appointment, is_approved=False)

            # Make the associated time slot available again
            time_slot = appointment.time_slot
            time_slot.status = 'AVAILABLE'
            time_slot.save()
            

            return redirect('therapist_appointments')

    has_notification = request.user.appointments.filter(status_change_notification=True).exists()

    return render(request, 'therapist_approve_appointment.html', {'appointment': appointment})

def send_approval_notification(appointment, is_approved=True):
    if is_approved:
        subject = 'Your appointment has been approved'
        template_name = 'approval_email_template.html'
    else:
        subject = 'Your appointment has been rejected'
        template_name = 'rejection_email_template.html'

    message = render_to_string(template_name, {'appointment': appointment})
    plain_message = strip_tags(message)
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = appointment.user.email

    # Send the email
    send_mail(subject, plain_message, from_email, [to_email], html_message=message)




# views.py
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Appointment

@require_POST
def remove_appointment(request):
    appointment_id = request.POST.get('appointment_id')

    try:
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.delete()
        return JsonResponse({'success': True})
    except Appointment.DoesNotExist:
        return JsonResponse({'success': False})
    
# February 26
# views.py

# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Appointment

@login_required
def view_appointment_status(request):
    user = request.user
    appointments = Appointment.objects.filter(user=user)
    return render(request, 'view_appointment_status.html', {'appointments': appointments})



# views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Appointment

def delete_appointment(request):
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')

        try:
            # Assuming you have an Appointment model with an 'id' field
            appointment = get_object_or_404(Appointment, id=appointment_id)

            # Implement your logic to delete the appointment based on the appointment_id
            appointment.delete()

            # Return a JSON response to the AJAX request
            return JsonResponse({'status': 'success'})
        except Exception as e:
            # Handle exceptions (e.g., invalid appointment_id or deletion error)
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    


from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from razorpay import Client
from django.conf import settings
from .models import Appointment

razorpay_api_key = settings.RAZORPAY_API_KEY
razorpay_secret_key = settings.RAZORPAY_API_SECRET

razorpay_client = Client(auth=(razorpay_api_key, razorpay_secret_key))

@csrf_exempt
def new_payment(request):
    if request.method == 'POST':
        # Get the data sent in the request
        data = request.POST

        # Extract payment_id and appointment_id
        payment_id = data.get('payment_id')
        appointment_id = data.get('appointment_id')

        print("Payment ID:", payment_id)
        print("Appointment ID:", appointment_id)

        # Fetch the appointment object and update payment status and payment_id
        try:
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.payment_status = 'PAID'
            appointment.payment_id = payment_id  # Assign payment_id to the appointment
            appointment.save()
            # Create a Razorpay order
            amount = 1000  # Example amount, you can change this dynamically based on your logic
            order_data = {
                'amount': amount,
                'currency': 'INR',
                'receipt': 'order_rcptid_11',
                'payment_capture': '1',  # Auto-capture payment
            }
            order = razorpay_client.order.create(data=order_data)
            context = {
                'razorpay_api_key': razorpay_api_key,
                'amount': order_data['amount'],
                'currency': order_data['currency'],
                'order_id': order['id'],
            }
            return render(request, 'new_payment.html', context)
        except Appointment.DoesNotExist:
            return JsonResponse({'error': 'Appointment not found.'}, status=404)
    else:
        # If it's a GET request, render the new_payment.html template
        return render(request, 'new_payment.html')

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_pdf_content(appointment):
    styles = getSampleStyleSheet()

    content = []

    # Add title
    title_text = f"Receipt for Appointment ID: {appointment.id}"
    title = Paragraph(title_text, styles['Title'])
    content.append(title)

    mind_ease_heading_text = "Mind Ease"
    mind_ease_heading = Paragraph(mind_ease_heading_text, styles['Heading1'])
    content.append(mind_ease_heading)


    # Add a spacer for separation
    content.append(Spacer(1, 12))

    # Add appointment details with improved styling
    user_text = f"<font color='blue'><b>User:</b></font> {appointment.user.username}"
    therapist_text = f"<font color='blue'><b>Therapist:</b></font> {appointment.therapist.username}"
    time_slot_text = f"<font color='blue'><b>Time Slot:</b></font> {appointment.time_slot.start_time} to {appointment.time_slot.end_time}"
    payment_status_text = f"<font color='blue'><b>Payment Status:</b></font> {appointment.payment_status}"

    user = Paragraph(user_text, styles['BodyText'])
    therapist = Paragraph(therapist_text, styles['BodyText'])
    time_slot = Paragraph(time_slot_text, styles['BodyText'])
    payment_status = Paragraph(payment_status_text, styles['BodyText'])

    content.extend([user, therapist, time_slot, payment_status])

    # Add a spacer for separation
    content.append(Spacer(1, 24))

    return content





def download_receipt(request, appointment_id):
    # Retrieve the appointment object
    appointment = get_object_or_404(Appointment, id=appointment_id)

    # Generate PDF content
    content = generate_pdf_content(appointment)

    try:
        # Create an HttpResponse object with PDF content
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="receipt_{appointment_id}.pdf"'

        # Create PDF document
        doc = SimpleDocTemplate(response, pagesize=letter)
        doc.build(content)

        return response
    except Exception as e:
        # Log the error or handle it appropriately
        print(f"Error generating PDF: {e}")
        # Return an error response or redirect to an error page
        return HttpResponse("Error generating PDF. Please try again later.", status=500)



# from django.shortcuts import redirect
# import razorpay
# from django.conf import settings

# def generate_payment_request(request):
#     if request.method == 'POST':
#         # Initialize Razorpay client with your API key
#         client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

#         # Extract necessary data from the request
#         time_slot_id = request.POST.get('time_slot_id')

#         # Calculate the amount based on time slot details or any other criteria
#         amount = 1000  # Example amount in paisa (e.g., 1000 paisa = Rs. 10)

#         # Create a Razorpay order
#         razorpay_order = client.order.create({
#             'amount': amount,
#             'currency': 'INR',
#             'payment_capture': 1  # Auto-capture payment after order creation
#             # Add additional parameters as required by your payment gateway
#         })

#         # Extract the order ID from the Razorpay order response
#         order_id = razorpay_order['id']

#         # Optionally, you may save the order ID or other details in your database for reference

#         # Redirect the user to the Razorpay checkout page with the order ID
#         return redirect(f"https://checkout.razorpay.com/v1/payment?order_id={order_id}")

#     # If the request method is not POST, handle it accordingly (e.g., return an error response)
#     return HttpResponseBadRequest("Invalid request method")



# views.py

from django.shortcuts import render, redirect
from django.conf import settings
from .models import Order
from razorpay import Client

razorpay_api_key = settings.RAZORPAY_API_KEY
razorpay_secret_key = settings.RAZORPAY_API_SECRET

razorpay_client = Client(auth=(razorpay_api_key, razorpay_secret_key))

def new_paymenttok(request):
    if request.method == 'POST':
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        if razorpay_payment_id:
            # Payment successful, redirect to home page
            return redirect('/')
        else:
            # Payment failed, handle accordingly
            return render(request, 'payment_failed.html')  # Render a template for failed payment
    else:
        # Create a Razorpay order
        amount = 10000  # Example amount, you can change this dynamically based on your logic
        order_data = {
            'amount': amount,
            'currency': 'INR',
            'receipt': 'order_rcptid_11',
            'payment_capture': '1',  # Auto-capture payment
        }
        order = razorpay_client.order.create(data=order_data)
        
        # Save order details to the database
        Order.objects.create(
            order_id=order['id'],
            amount=order_data['amount'],
            currency=order_data['currency']
        )
        
        context = {
            'razorpay_api_key': razorpay_api_key,
            'amount': order_data['amount'],
            'currency': order_data['currency'],
            'order_id': order['id'],
        }
        return render(request, 'new_paymenttok.html', context)

# Implementing Emotion Detection
# views.py
# from django.shortcuts import render
# import cv2
# import numpy as np
# import tensorflow_hub as hub

# def index(request):
#     detect_emotions()
#     return render(request, 'index.html')

# def detect_emotions():
#     try:
#         # Load the pre-trained Haar cascade for face detection
#         face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#         # Load the FER model from TensorFlow Hub
#         # Load the FER model from TensorFlow Hub
#         fer_model = hub.load("https://tfhub.dev/google/on_device_vision/classifier/emotion_classifier_autoflip/1")

#         print("FER model loaded successfully!")
#     except Exception as e:
#         print("Error loading FER model:", e)
#         return

#     # Open video capture device (0 for webcam)
#     cap = cv2.VideoCapture(0)

#     while True:
#         # Capture frame-by-frame
#         ret, frame = cap.read()

#         # Convert the frame to grayscale for face detection
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         # Detect faces in the frame
#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
#         # Draw rectangles around the detected faces and label emotions
#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

#             # Perform emotion detection on each face region
#             emotion = detect_single_emotion(gray[y:y+h, x:x+w], fer_model)
#             cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

#         # Convert the frame to JPEG format
#         _, jpeg = cv2.imencode('.jpg', frame)

#         # Send the JPEG frame to the web interface via Django channels or other means

#         # Break the loop if 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the capture device
#     cap.release()

# def detect_single_emotion(face_region, fer_model):
#     emotions = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]

#     # Resize input frame to match model input size (48x48 pixels)
#     resized_face = cv2.resize(face_region, (48, 48))

#     # Normalize pixel values to [0, 1]
#     normalized_face = resized_face / 255.0

#     # Expand dimensions to match model input shape
#     input_tensor = np.expand_dims(normalized_face, 0)

#     # Perform inference
#     predictions = fer_model(input_tensor)

#     # Get the predicted emotion label
#     emotion_index = np.argmax(predictions[0])
#     return emotions[emotion_index]




# new testing 
from django.shortcuts import render
import cv2
from deepface import DeepFace

def emotion_detection(request):
    # Open video capture device (0 for webcam)
    cap = cv2.VideoCapture(0)

    # Initialize face count
    total_faces_detected = 0

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Detect faces in the frame
        faces = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml').detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Update total face count
        total_faces_detected = len(faces)

        # Process each detected face
        for (x, y, w, h) in faces:
            # Perform emotion classification
            face = frame[y:y+h, x:x+w]
            result = DeepFace.analyze(face, enforce_detection=False)

            # Ensure that result is not an empty list
            if result:
                # Assuming the first element of the list contains the dominant emotion
                emotion = result[0]['dominant_emotion']

                # Overlay detected emotion on the frame
                cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

            # Draw rectangle around the detected face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Display the total face count
        cv2.putText(frame, f"Total Faces Detected: {total_faces_detected}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

        # Display the resulting frame
        cv2.imshow('Real-time Emotion Detection', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture device and close all windows
    cap.release()
    cv2.destroyAllWindows()

    return render(request, 'emotion_detection.html')



