from rest_framework import serializers
from .models import County

class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = ('id', 'county', 'doc_type')
