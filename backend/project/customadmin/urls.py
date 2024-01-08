# accounts/urls.py
from django.urls import path
from .views import AdminLoginView,UserListView,HotelListView,ToggleHotelAvailabilityView,HotelUpdateView
from . import views
urlpatterns = [
    # Your existing URLs
    path('admin-login/', AdminLoginView.as_view(), name='admin-login'),
    path('user-list/',UserListView.as_view(),name='user-list'),
    path('admin/user/<int:pk>/block/', views.admin_block_user, name='admin-user-block'),
    path('admin/user/<int:pk>/unblock/',views.admin_unblock_user, name='admin-user-unblock'),
    path('hotel-details/',HotelListView.as_view(), name='hotel_details'),
    path('hotel-details/<int:id>/', ToggleHotelAvailabilityView.as_view(), name='toggle_hotel_availability'),
    path('hotel-details/<int:pk>/update/', HotelUpdateView.as_view(), name='hotel-update'),
    path('customadmin/hotel-details/detail/<int:hotel_id>/', views.get_hotel_details, name='get-hotel-details'),




    

]
