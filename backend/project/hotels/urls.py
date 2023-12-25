# accounts/urls.py
from django.urls import path
from .views import HotelListView

urlpatterns = [
    # Your existing URLs
    path('hotels/', HotelListView.as_view(), name='hotel-list'),
]
