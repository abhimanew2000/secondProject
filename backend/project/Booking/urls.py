# Booking/urls.py

from django.urls import path
from . import views
urlpatterns = [
    path('initiate_razorpay_payment/', views.hotel_booking, name='initiate-razorpay-payment'),
    path('confirm_booking/', views.confirm_booking, name='confirm-booking'),
    path('cancel-booking/<int:bookingId>/', views.cancel_booking, name='confirm-booking'),

]
