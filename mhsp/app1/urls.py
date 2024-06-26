from django.urls import path
from . import views
from .views import display_image
from django.contrib.auth import views as auth_views
from .views import therapist_list, feedback_form, therapist_feedback

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
    #path('toggleUserStatus/', views.toggleUserStatus, name='toggleUserStatus'),
    path('update_profile/', views.update_profile, name='update_profile'),
    #path('product/', views.product, name='product'),
    path('add_product/', views.add_product, name='add_product'),
    path('product_list/', views.product_list, name='product_list'),

    path('product/edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('product/delete/<int:pk>/', views.delete_product, name='delete_product'),

    path('ProductForUser/', views.ProductForUser, name='ProductForUser'), # this is build for showing items to users
    path('product_list_view/', views.product_list_view, name='product_list_view'), #remove
    
    #path('buy_product/<int:product_id>/',views.buy_product, name='buy_product'),
    path('add_to_cart/<int:product_id>/',views.add_to_cart, name='add_to_cart'),
    path('cart/',views.add_to_cart_page, name='add_to_cart_page'),
    path('update_cart_quantity/<int:cart_id>/<str:action>/',views.update_cart_quantity, name='update_cart_quantity'),


    #path('product/buy/<int:pk>/', views.buy_product, name='buy_product'),
    #path('product/add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    
    #path('Tdash/',views.Tdash,name='Tdash'),

    
    path('Tdash/',views.Tdash,name='Tdash'),
    path('therapists/', views.therapist_list, name='therapist_list'),
    path('therapists/<int:therapist_id>/update/', views.update_therapist, name='update_therapist'),
    path('image/', display_image, name='display_image'),
    path('displayTherapist/',views.displayTherapist, name='displayTherapist'),
    path('user-list/', views.user_list, name='user_list'),
    path('activate-user/<int:user_id>/', views.activate_user, name='activate_user'),
    path('deactivate-user/<int:user_id>/', views.deactivate_user, name='deactivate_user'),
    path('therapist_list_new/', views.therapist_list_new, name='therapist_list_new'),
    path('approve-therapist/<int:therapist_id>/', views.approve_therapist, name='approve_therapist'),
    # path('book_appointment/<int:therapist_id>/', views.book_appointment, name='book_appointment'),
    # path('therapist_appointments/', views.therapist_appointments, name='therapist_appointments'),
    # path('approve_appointment/<int:appointment_id>/', views.approve_appointment, name='approve_appointment'),
    # path('successappo/',views.successappo,name='successappo'),


    path('therapist-list/', therapist_list, name='therapist_list'),
    path('feedback/<int:therapist_id>/',feedback_form, name='feedback_form'),
    path('therapist-feedback/<int:therapist_id>/', therapist_feedback, name='therapist_feedback'),
    path('add_article/', views.add_article, name='add_article'),
    path('article_list/', views.article_list, name='article_list'),


    # path('schedule_appointment/',views.schedule_appointment, name='schedule_appointment'),
    # path('appointment_list/',views.appointment_list, name='appointment_list'),

    path('write_experience/',views.write_experience, name='write_experience'),
    path('experience_list/',views.experience_list, name='experience_list'),

    path('edit_experience/<int:experience_id>/',views.edit_experience, name='edit_experience'),
    path('delete_experience/<int:experience_id>/',views.delete_experience, name='delete_experience'),
    path('supportplatform/', views.supportplatform, name='supportplatform'),
    path('payment/', views.rentnxt, name='payment'),

    #path('therapist_profile/', views.therapist_profile, name='therapist_profile'),
    path('add_time_slot/', views.add_time_slot, name='add_time_slot'),
    path('view_time_slots/', views.view_time_slots, name='view_time_slots'),
    path('new_view_time_slots/', views.new_view_time_slots, name='new_view_time_slots'),
    path('edit_time_slot/<int:time_slot_id>/', views.edit_time_slot, name='edit_time_slot'),
    path('delete_time_slot/<int:time_slot_id>/', views.delete_time_slot, name='delete_time_slot'),

    path('threads/', views.ThreadListView.as_view(), name='thread_list'),
    path('thread/<int:thread_id>/', views.ThreadDetailView.as_view(), name='thread_detail'),
    path('create_thread/', views.CreateThreadView.as_view(), name='create_thread'),
    path('thread/<int:thread_id>/create_post/', views.CreatePostView.as_view(), name='create_post'),
    path('threads/<str:username>/', views.UserThreadListView.as_view(), name='thread_list_user'),

    path('book-appointment/<int:time_slot_id>/', views.book_appointment, name='book_appointment'),
    path('therapist-appointments/', views.therapist_appointments, name='therapist_appointments'),
    path('approve-appointment/<int:appointment_id>/', views.approve_appointment, name='approve_appointment'),
    path('therapist-approve-appointment/<int:appointment_id>/', views.therapist_approve_appointment, name='therapist_approve_appointment'),
    path('remove_appointment/', views.remove_appointment, name='remove_appointment'),
    path('view_appointment_status/', views.view_appointment_status, name='view_appointment_status'),
    path('delete_appointment/', views.delete_appointment, name='delete_appointment'),
    path('new_payment/', views.new_payment, name='new_payment'),
    path('new_paymenttok/', views.new_paymenttok, name='new_paymenttok'),
    path('download_receipt/<int:appointment_id>/', views.download_receipt, name='download_receipt'),
    #path('generate_payment_request', views.generate_payment_request, name='generate_payment_request'),
    path('generate_pdf_content/', views.generate_pdf_content, name='generate_pdf_content'),
    path('send_approval_notification/', views.send_approval_notification, name='send_approval_notification'),
   
]
