
from django.db import models
from rest_framework import serializers
from .models import User, Station, Cycle

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_id',
            'username',
            'date_created',
        ]
class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = [
            'station_id',
            'station_name',
        ]
class CycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cycle
        fields = [
            'cycle_id',
            'borrowed_user',
            'station_id',
        ]