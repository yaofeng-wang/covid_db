from rest_framework import serializers
from dashboard.models import Record

class RecordSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Record
        fields = ['date', 'num_imported', 'num_dormitories', 'num_community']
