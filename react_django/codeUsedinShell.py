# #!/usr/bin/env python3
from cars.models import Car
from persons.models import Person
from faker import Faker
from faker_vehicle import VehicleProvider
import random



faker = Faker()
faker.add_provider(VehicleProvider)
def print_random_model():
	print(faker.vehicle_make_model(), 111111111)

# for _ in range(0, 15):
# 	Car.objects.create(model=faker.vehicle_make_model(), number=faker.license_plate(), manufacturedate=faker.date_between())
# for _ in range(0, 10):
# 	Person.objects.create(name=faker.first_name(), surname=faker.last_name(), driverlicensenum=faker.nic_handle('DL'), birthdate=faker.date_between(80, 18))


# for id in range(1, personscount):
# 	person = Person.objects.get(pk=id)
# 	cars_per_person = random.randint(0, 3)
# 	for num in range (0, cars_per_person):
# 		random_car_id = random.randint(1, cars_count)
# 		person.cars.add(Car.objects.get(id=random_car_id))
