from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CountySerializer
from .models import County, DocType, DateRange

# Create your views here.

class CountyView(viewsets.ModelViewSet):
    serializer_class = CountySerializer
    queryset = County.objects.all()

class DocView(viewsets.ModelViewSet):
    serializer_class = CountySerializer
    queryset = DocType.objects.all()

class DateView(viewsets.ModelViewSet):
    serializer_class = CountySerializer
    queryset = DateRange.objects.all()
