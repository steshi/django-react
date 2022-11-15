from django.db import models
from datetime import date
from cars.models import Car

# Create your models here.
class Person(models.Model):
	name = models.CharField("First name", max_length=30)
	surname = models.CharField("Last name", max_length=30)
	driverlicensenum = models.CharField(max_length=12)
	birthdate = models.DateField(default=date.today )
	cars = models.ManyToManyField(Car)
	def __str__(self):
		return self.name
