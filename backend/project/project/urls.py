
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('accounts.urls')),
    # path('api/', include('hotels.urls')),  # Include hotels URLs here

]
