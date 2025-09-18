from django.shortcuts import render
from .serializers import SafetyValveSerializer
from rest_framework import generics
from .models import SafetyValve

class SafetyValveList(generics.ListAPIView):
    queryset = SafetyValve.objects.all()
    serializer_class = SafetyValveSerializer
    
class SafetyValveCreate(generics.CreateAPIView):
    queryset = SafetyValve.objects.all()
    serializer_class = SafetyValveSerializer