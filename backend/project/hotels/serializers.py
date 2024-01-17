# hotels/serializers.py
from rest_framework import serializers
from .models import Hotel,Room,RoomType

class HotelSerializer(serializers.ModelSerializer):
    multiimage = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['id','name', 'description', 'city', 'address', 'image', 'availability', 'amenities', 'ratings', 'price', 'multiimage']
    
    
    def get_multiimage(self, obj):
        return [image.url for image in obj.multiimage.all()] if obj.multiimage.exists() else []
    


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