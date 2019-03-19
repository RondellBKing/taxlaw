from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CountySerializer, DocSerializer, DateSerializer
from .models import County, DocType, DateRange

# Create your views here.

class CountyView(viewsets.ModelViewSet):
    serializer_class = CountySerializer
    queryset = County.objects.all()

class DocView(viewsets.ModelViewSet):
    serializer_class = DocSerializer
    queryset = DocType.objects.all()

class DateView(viewsets.ModelViewSet):
    serializer_class = DateSerializer
    queryset = DateRange.objects.all()
    
