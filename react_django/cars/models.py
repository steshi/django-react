from django.db import models
from datetime import date

# Create your models here.
class Car(models.Model):
	model = models.CharField("First name", max_length=40)
	number = models.CharField(max_length=10)
	manufacturedate = models.DateField(default=date.today)

	def __str__(self):
		return self.model