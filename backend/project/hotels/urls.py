# accounts/urls.py
from django.urls import path
from .views import AutocompleteCityView,HotelList
from django.urls import re_path

from . import views
urlpatterns = [
    # Your existing URLs
    path('hotels/', HotelList.as_view(), name='hotel-list'),
    path('autocomplete_city/', AutocompleteCityView.as_view(), name='autocomplete-city'),
re_path(r'^get-hotels/$', views.get_hotels, name='get-hotels'),
path('hotels/about/<int:hotel_id>/', views.get_hotel_details, name='get-hotel-details'),
path('get-hotel-images/<int:hotel_id>/',views.get_hotel_images, name='get_hotel_images'),



]
