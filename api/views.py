from django.shortcuts import render
from rest_framework import generics, permissions, filters
from .serializers import UserSerializer,StationSerializer,CycleSerializer
from .models import User, Station, Cycle
from api import serializers
# Create your views here.
class UsersList(generics.ListAPIView):
    """
    Retrieve all daily cases
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering_fields = ['date_created']
    ordering = ['-date_created']

class StationsList(generics.ListAPIView):
    """
    Retrieve all daily cases
    """
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering_fields = ['date_created']
    ordering = ['-date_created']

class CyclesList(generics.ListAPIView):
    """
    Retrieve all daily cases
    """
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering_fields = ['date_created']
    ordering = ['-date_created']