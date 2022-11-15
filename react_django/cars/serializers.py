from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('pk', 'model', 'number', 'manufacturedate')

class CarShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('model', 'number')