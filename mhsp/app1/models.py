from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        THERAPIST = "THERAPIST", "Therapist"
        USER = "USER", "User"

    role = models.CharField(max_length=50, choices=Role.choices)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    qualification = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    specialization = models.CharField(max_length=255, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    is_therapist = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
   

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.username
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name




class Feedback(models.Model):
    therapist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='therapist_feedback')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_feedback')
    rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} feedback for {self.therapist.username}"



class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='article_images/')






# Add a new model to represent user experiences
class UserExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"


# models.py
from django.conf import settings
from django.db import models
from django.utils import timezone

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s Cart"



# time slot
    
class TimeSlot(models.Model):
    class SessionType(models.TextChoices):
        MORNING = "MORNING", "Morning Session"
        AFTERNOON = "AFTERNOON", "Afternoon Session"

    TIME_SLOTS = [
        ("8-9", "8:00 AM - 9:00 AM"),
        ("9-10", "9:00 AM - 10:00 AM"),
        ("10-11", "10:00 AM - 11:00 AM"),
        ("12-1", "12:00 PM - 1:00 PM"),
        ("1-2", "1:00 PM - 2:00 PM"),
        ("2-3", "2:00 PM - 3:00 PM"),
        ("3-4", "3:00 PM - 4:00 PM"),
    ]
    
    therapist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='available_time_slots')
    time_slot = models.CharField(max_length=5, choices=TIME_SLOTS, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    session_type = models.CharField(max_length=50, choices=SessionType.choices, null=True)
    is_booked = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.therapist.username}'s {self.get_session_type_display()} Time Slot {self.start_time} - {self.end_time}"





from django.db import models
from django.contrib.auth import get_user_model

class Thread(models.Model):
    title = models.CharField(max_length=255)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    therapist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approved_appointments')
    time_slot = models.ForeignKey('TimeSlot', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved')], default='PENDING')
    status_change_notification = models.BooleanField(default=False)

    PAYMENT_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('FAILED', 'Failed'),
    ]
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='PENDING')

    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)

    payment_id = models.CharField(max_length=100, blank=True, null=True)



    def __str__(self):
        return f"Appointment: {self.user.username} with {self.therapist.username} at {self.time_slot.start_time}"
    
    def is_approved(self):
        return self.status == 'APPROVED'
    

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Order(models.Model):
    order_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='paid_orders')
    payment_status = models.CharField(max_length=20, choices=[('PENDING', 'Pending'), ('PAID', 'Paid'), ('FAILED', 'Failed')], default='PENDING')

    def __str__(self):
        return f"Order {self.order_id}"

    


