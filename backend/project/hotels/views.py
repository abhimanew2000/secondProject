# accounts/views.py
from rest_framework import generics
from .models import Hotel
from .serializers import HotelSerializer
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404

from django.views import View

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,ListAPIView
from .models import Room, RoomType
from .serializers import RoomSerializer, RoomTypeSerializer,HotelsSerializer

# hotels/views.py


class HotelList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelsSerializer


class RoomTypeList(ListAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer

class AutocompleteCityView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', '').strip()
        print('Received Query:', repr(query))

        # Use case-insensitive filtering on the 'city' field
        cities = Hotel.objects.filter(Q(city__iexact=query) | Q(city__icontains=query)).values_list('city', flat=True)

        print('Filtered Cities:', cities)
        return JsonResponse(list(cities), safe=False)
    
# views.py
@require_GET
def get_hotels(request):
    print('hiiii')
    
    city = request.GET.get('city')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    print('city:', city)
    print('min_price:', min_price)
    print('max_price:', max_price)
    queryset = Hotel.objects.filter(city=city)

    if min_price is not None and max_price is not None:
        queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        print(queryset, "qqqqqqq")

    # Assuming you have a serializer named HotelSerializer
    serializer = HotelSerializer(queryset, many=True)

    return JsonResponse({'hotels': serializer.data})

@require_GET
def get_hotel_details(request, hotel_id):
    try:
        hotel = Hotel.objects.get(id=hotel_id)
        
    except Hotel.DoesNotExist:
        raise Http404("Hotel does not exist")

    # Assuming you have a serializer named HotelSerializer
    serializer = HotelSerializer(hotel)

    return JsonResponse({'hotel': serializer.data})


def get_hotel_images(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)

    data = {
        'hotel_image': hotel.image.url if hotel.image else None,
        'room_type_images': [room_type.image.url for room_type in hotel.room_types.all() if room_type.image],
        'room_images': [room.image.url for room in hotel.rooms.all() if room.image],
    }

    return JsonResponse(data)