from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import ListAPIView
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

# @api_view(['GET'])
# def hotel_list_search(request):
#     city = request.query_params.get('city')
#     hotels = Hotel.objects.all()
#     if city:
#           hotels= hotels.filter(city__iexact=city)
#     serializer = HotelSerializer(hotels,many=True)
#     return Response(serializer.data)
