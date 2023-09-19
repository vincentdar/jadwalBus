from django.shortcuts import render
from django.http import JsonResponse
from .models import Route
from .serializers import BusRouteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def RouteList(request):
    bus_routes = Route.objects.all()
    serializer = BusRouteSerializer(bus_routes, many=True)
    return Response(serializer.data)

api_view(['GET'])
def RouteDetail(request, pk):
    bus_routes = Route.objects.get(pk=pk)
    serializer = BusRouteSerializer(bus_routes)
    return Response(serializer.data)

api_view(['POST'])
def AddRoute(request):
    serializer = BusRouteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

api_view(['PUT'])
def UpdateRoute(request, pk):
    route = Route.objects.get(id=pk)
    serializer = BusRouteSerializer(instance=route, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

api_view(['DELETE'])
def DeleteRoute(request, pk):
    route = Route.objects.get(id=pk)
    route.delete()
    return Response("Routes successfully deleted!")