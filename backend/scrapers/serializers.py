from rest_framework import serializers
from .models import County, Lien

class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = ('id', 'county')

class LienSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lien
        fields = ('id', 'recording_date', 'doc_title', 'involved')

# class DateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DateRange
#         fields = ('id', 'start_date', 'end_date')
