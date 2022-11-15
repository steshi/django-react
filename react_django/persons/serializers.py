from rest_framework import serializers
from .models import Person
# from cars.models import Car

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('pk','name', 'surname', 'driverlicensenum', 'birthdate', 'cars')
