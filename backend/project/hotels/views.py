# accounts/views.py
from rest_framework import generics
from .models import Hotel
from .serializers import HotelSerializer
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.db.models import Q

from django.views import View



# hotels/views.py


class HotelList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer




class AutocompleteCityView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', '').strip()
        print('Received Query:', repr(query))

        # Use case-insensitive filtering on the 'city' field
        cities = Hotel.objects.filter(Q(city__iexact=query) | Q(city__icontains=query)).values_list('city', flat=True)

        print('Filtered Cities:', cities)
        return JsonResponse(list(cities), safe=False)
    
# views.py

def get_hotels(request):
    print('hefvsd')
    city_name = request.GET.get('city', '')
    hotels =list( Hotel.objects.filter(city__iexact=city_name).values())
    print(hotels,'hotels')

    return JsonResponse({'city_name': city_name, 'hotels': hotels})
