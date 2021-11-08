from rest_framework import generics, permissions, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, StationSerializer, CycleSerializer
from .models import User, Station, Cycle
from api import serializers
import jwt, datetime


# Create your views here.

@api_view(['GET'])
def getUser(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)
        



@api_view(['POST'])
def SignUp(request):
    if request.method == 'POST':
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
def Login(request):
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
def getStasion(request):
    station = Station.objects.all()
    serializer = StationSerializer(station, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCycle(request):
    cycle = Cycle.objects.all()
    serializer = CycleSerializer(cycle, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def updateUser(request, pk):
    data = request.data

    user = User.objects.get(user_id=pk)

    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(user_id=pk)
    user.delete()
    return Response('user telah dihapus')
