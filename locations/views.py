from django.shortcuts import render
from rest_framework import generics
from .models import Location
from .serializer import LocationSerializer
from .permissions import IsOwnerOrReadOnly

class LocationList(generics.ListCreateAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Location.objects.all()
  serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Location.objects.all()
  serializer_class = LocationSerializer

