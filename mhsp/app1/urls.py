from django.urls import path
from . import views
from .views import display_image
from django.contrib.auth import views as auth_views

from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns=[

    path('signup/',views.signup,name='signup'),
    path('', views.user_login, name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.logoutPage,name='logout'),
    path('thrpreg/',views.ThreapistReg,name='thrpreg'),
    path('custom_admin_page/',views.custom_admin_page,name='custom_admin_page'),
    path('edit/',views.EditProfile,name='edit'),
    path('password_reset', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('toggleUserStatus/', views.toggleUserStatus, name='toggleUserStatus'),
    path('update_profile/', views.update_profile, name='update_profile'),
    #path('product/', views.product, name='product'),
    path('add_product/', views.add_product, name='add_product'),
    path('product_list/', views.product_list, name='product_list'),

    path('product/edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('product/delete/<int:pk>/', views.delete_product, name='delete_product'),

    path('ProductForUser/', views.ProductForUser, name='ProductForUser'), # this is build for showing items to users
    path('product_list_view/', views.product_list_view, name='product_list_view'), #remove
    path('product/buy/<int:pk>/', views.buy_product, name='buy_product'),
    path('product/add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    
    #path('Tdash/',views.Tdash,name='Tdash'),
    path('Tdash/',views.Tdash,name='Tdash'),
    path('therapists/', views.therapist_list, name='therapist_list'),
    path('therapists/<int:therapist_id>/update/', views.update_therapist, name='update_therapist'),
    path('image/', display_image, name='display_image'),
    path('displayTherapist/',views.displayTherapist, name='displayTherapist'),

]