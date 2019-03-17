from rest_framework import serializers
from .models import County, DocType, DateRange

class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = ('id', 'county')

class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocType
        fields = ('id', 'doc_type')

class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateRange
        fields = ('id', 'start_date', 'end_date')
