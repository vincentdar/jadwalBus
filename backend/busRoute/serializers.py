from rest_framework import serializers
from .models import Route

class BusRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('id',
                  'bus',
                  'route',
                  'departure_terminal',
                  'destination_terminal',
                  'time_departure',
                  'time_arrival',
                  'seat',
                  'price'
                  )
        
        