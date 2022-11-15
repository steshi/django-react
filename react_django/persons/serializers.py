from rest_framework import serializers
from .models import Person
from cars.serializers import CarShortSerializer

# from cars.models import Car
# cars = serializers.PrimaryKeyRelatedField(many=True)
class PersonSerializer(serializers.ModelSerializer):
    # cars = CarSerializer(read_only=True, many=True)

    class Meta:
        model = Person
        fields = ('pk', 'name', 'surname', 'driverlicensenum', 'birthdate')

class RelSerializer(serializers.ModelSerializer):
    cars = CarShortSerializer(read_only=True, many=True)
    
    class Meta:
        model = Person
        fields = ('pk','name', 'surname', 'driverlicensenum', 'cars')