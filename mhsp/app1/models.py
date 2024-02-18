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


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_appointments')
    therapist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='therapist_appointments')
    appointment_date = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_therapist = models.BooleanField(default=False)
    

    def __str__(self):
        return f"Appointment between {self.user.username} and {self.therapist.username} on {self.appointment_date}"
    


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



class Schedule(models.Model):  # Changed from Appointment to Schedule
    therapist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='therapist_schedules')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_schedules')
    date_time = models.DateTimeField()
    duration = models.PositiveIntegerField()



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

    therapist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='available_time_slots')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    session_type = models.CharField(max_length=50, choices=SessionType.choices, null=True)

    def __str__(self):
        return f"{self.therapist.username}'s {self.get_session_type_display()} Time Slot {self.start_time} - {self.end_time}"
    

