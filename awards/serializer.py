from dataclasses import field, fields
from rest_framework import serializers
from .models import Awards

class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awards
        fields = ('title','description','link')