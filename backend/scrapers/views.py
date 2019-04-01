from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CountySerializer, LienSerializer
from .models import County, Lien

# Create your views here.

class CountyView(viewsets.ModelViewSet):
    serializer_class = CountySerializer
    queryset = County.objects.all()

class LienView(viewsets.ModelViewSet):
    serializer_class = LienSerializer
    queryset = Lien.objects.all()

# class DateView(viewsets.ModelViewSet):
#     serializer_class = DateSerializer
#     queryset = DateRange.objects.all()
