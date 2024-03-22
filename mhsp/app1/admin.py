from django.contrib import admin

from .models import User
from .models import Order
admin.site.register(User)
admin.site.register(Order)


# Register your models here.
