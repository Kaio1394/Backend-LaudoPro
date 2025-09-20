from django.shortcuts import render
from rest_framework import generics
from .serializers import WorkOrderSerializer
from .models import WorkOrder

class WorkOrderlist(generics.ListAPIView):
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer
