from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns=[

    path('signup/',views.signup,name='signup'),
    path('',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.logoutPage,name='logout'),
    path('thrpreg/',views.ThreapistReg,name='thrpreg'),
    path('demo/',views.TherapHome,name='demo'),
    
    path('password_reset', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]