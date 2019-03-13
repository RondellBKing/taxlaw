from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CountySerializer
from .models import County

# Create your views here.

class CountyView(viewsets.ModelViewSet):
    serializer_class = CountySerializer
    queryset = County.objects.all()
