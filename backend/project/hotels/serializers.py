# hotels/serializers.py
from rest_framework import serializers
from .models import Hotel,Room,RoomType

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

    
   
    


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
    

class HotelsSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)
    room_types = RoomTypeSerializer(many=True, read_only=True,)
    class Meta:
        model = Hotel
        fields = '__all__'
        extra_kwargs = {
            'image': {'required': False}
        }

