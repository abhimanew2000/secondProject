from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView
from accounts.models import User
from .serializers import UserSerializers
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser
from hotels.models import Hotel
from rest_framework.decorators import api_view, permission_classes
from hotels.serializers import HotelSerializer

from rest_framework.generics import ListCreateAPIView

from django.http import JsonResponse
from django.views import View

# Create your views here.

class AdminLoginView(APIView):
    def post(self, request, format=None):
        email = request.data.get("email")
        print('email',email)
        password = request.data.get("password")
        print('password',password)
        user = authenticate(email=email, password=password)

        if user and user.is_staff:
            return Response({"msg": "Admin Login Success", "user_email": user.email}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"errors": {"non_field_errors": ["Invalid admin credentials"]}},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    # permission_classes =[IsAuthenticated]


@api_view(['PUT'])
def admin_block_user(request, pk):
    print(request.user, 'user')
    print(request.user.id, 'idd')

    user = get_object_or_404(User, id=pk)
    user.is_active = False
    user.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['PUT'])
def admin_unblock_user(request, pk):
        user = get_object_or_404(User, id=pk)
        user.is_active = True  # Set is_active to True to unblock the user
        user.save()
        return Response(status=status.HTTP_200_OK)

class HotelListView(ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer 


class HotelDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class ToggleHotelAvailabilityView(APIView):
    def patch(self, request, id):
        try:
            hotel = Hotel.objects.get(id=id)
            serializer = HotelSerializer(hotel, data={'availability': not hotel.availability}, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': f'Toggled availability for hotel with ID: {id}'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Hotel.DoesNotExist:
            return Response({'error': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)




class HotelUpdateView(RetrieveUpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    lookup_field = 'pk'  # Add this line
 
    
    def get_object(self):
        hotel_id = self.kwargs.get('pk')
        return get_object_or_404(Hotel, id=hotel_id)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

def get_hotel_details(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    data = {
        'id': hotel.id,
        'name': hotel.name,
        'description': hotel.description,
        'city': hotel.city,
        'address': hotel.address,
        'image_url': hotel.image.url if hotel.image else None,
        'availability': hotel.availability,
        'amenities': hotel.amenities,
        'ratings': str(hotel.ratings),
        'price': hotel.price,
    }
    return JsonResponse(data)