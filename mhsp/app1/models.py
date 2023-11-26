from django.db import models
from django.contrib.auth.models import AbstractUser

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
    
