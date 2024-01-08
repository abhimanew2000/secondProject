# hotels/serializers.py
from rest_framework import serializers
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id','name', 'description', 'city', 'address', 'image', 'availability', 'amenities', 'ratings', 'price']
