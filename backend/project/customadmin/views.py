from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView,RetrieveAPIView
from accounts.models import User
from .serializers import UserSerializers
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser
from hotels.models import Hotel
from rest_framework.decorators import api_view, permission_classes
from hotels.serializers import HotelSerializer,HotelsSerializer

from rest_framework.generics import ListCreateAPIView

from django.http import Http404, JsonResponse
from django.views import View
from hotels .models import Room, RoomType
from hotels.serializers import RoomSerializer, RoomTypeSerializer

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
        user.is_active = True  
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
    serializer_class = HotelsSerializer
    lookup_field = 'pk'  # Add this line
 
    def put(self, request,*args, **kwargs):
        try:
            instance = self.get_object()  # Use the built-in get_object method
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.update(request, *args, **kwargs)
            return Response({'success': 'Hotel updated successfully'}, status=status.HTTP_200_OK)
        except Http404:
            return Response({'error': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)


from django.contrib.auth import logout

class AdminLogoutView(APIView):
    def post(self, request, format=None):
        # Check if the user is a superuser
        if request.user.is_authenticated and request.user.is_superuser:
            logout(request)
            return Response({"msg": "Admin Logout Success"}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"errors": {"non_field_errors": ["User is not a superuser or is not authenticated"]}},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        




class RoomListView(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomTypeListView(ListCreateAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer

class RoomTypeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer



class HotelDetailView(RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelsSerializer


def hotel_room_fetch(request, hotel_id):
    data = {}
    rooms = Room.objects.filter(hotel=hotel_id)
    room_data = []

    for room in rooms:
        room_data.append({
            'room_type': room.room_type.name,
            'price_per_night': room.price_per_night,
            # Add other room fields as needed
        })

    data['rooms'] = room_data
    return JsonResponse(data)