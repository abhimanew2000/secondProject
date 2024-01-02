# accounts/urls.py
from django.urls import path
from .views import AutocompleteCityView,HotelList

urlpatterns = [
    # Your existing URLs
    path('hotels/', HotelList.as_view(), name='hotel-list'),
    path('autocomplete_city/', AutocompleteCityView.as_view(), name='autocomplete-city'),

]
