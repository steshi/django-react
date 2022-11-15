#!/usr/bin/env python3

from cars.models import Car
from react_django.persons.models import Person
from faker import Faker
from faker_vehicle import VehicleProvider


# Person.objects.all().delete()
# Car.objects.all().delete()

faker = Faker()
faker.add_provider(VehicleProvider)

print(faker.name())
print(12341234234)
print(faker.vehicle_make_model())
for _ in range(0, 15):
	Car.objects.create(model=faker.vehicle_make_model(), number=faker.license_plate(), manufacturedate=faker.date_between())
for _ in range(0, 10):
	Person.objects.create(name=faker.first_name(), surname=faker.last_name(), driverlicensenum=faker.nic_handle('DL'), birthdate=faker.date_between(80, 18))