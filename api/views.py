from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .serializers import UserSerializer, StationSerializer, CycleSerializer
from .models import User, Station, Cycle
from api import serializers
import datetime
from django.contrib.auth.hashers import make_password
# import jwt
# Create your views here.

@api_view(['GET'])
def get_user(requets):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user_by_id(request, pk):
    user = User.objects.get(user_id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def register(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        password = make_password(request.data['password'])
        if serializer.is_valid():
            serializer.save(password=password)
            return Response(serializer.data)

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        data = request.data
        user = User.objects.filter(username=data['username']).values().first()
        if not user:
            return Response("User tidak ditemukan")

        if data['password'] != user['password']:
            return Response('Password Salah')
        
        payload = {
            'id': user['user_id'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        return Response({
            'jwt':token
        })

@api_view(['GET'])
def get_station(request):
    station = Station.objects.all()
    serializer = StationSerializer(station, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_cycle(request):
    cycle = Cycle.objects.all()
    serializer = CycleSerializer(cycle, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_user(request, pk):
    data = request.data

    user = User.objects.get(user_id=pk)

    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_user(request, pk):
    user = User.objects.get(user_id=pk)
    user.delete()
    return Response('user telah dihapus')
