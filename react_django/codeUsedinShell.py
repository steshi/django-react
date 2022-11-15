# #!/usr/bin/env python3

# from cars.models import Car
# from persons.models import Person
# from faker import Faker
# from faker_vehicle import VehicleProvider
# import random

# # Person.objects.all().delete()
# # Car.objects.all().delete()

# faker = Faker()
# faker.add_provider(VehicleProvider)


# for _ in range(0, 15):
# 	Car.objects.create(model=faker.vehicle_make_model(), number=faker.license_plate(), manufacturedate=faker.date_between())
# for _ in range(0, 10):
# 	Person.objects.create(name=faker.first_name(), surname=faker.last_name(), driverlicensenum=faker.nic_handle('DL'), birthdate=faker.date_between(80, 18))

# import random

# persons_count = Person.object.all().count()
# cars_count = Car.object.all().count()



# for id in range(1, personscount):
# 	person = Person.objects.get(pk=id)
# 	cars_per_person = random.randint(0, 3)
# 	for num in range (0, cars_per_person):
# 		random_car_id = random.randint(1, cars_count)
# 		person.cars.add(Car.objects.get(id=random_car_id))
