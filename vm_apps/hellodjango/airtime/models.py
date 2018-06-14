from django.db import models

# Create your models here.
class Athist(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateField(auto_now_add=True)
	amount = models.CharField(max_length=255)
	status = models.CharField(max_length=255)
	source = models.CharField(max_length=255)
	destination = models.CharField(max_length=255)
	def __str__(self):
		return self.amount

class Buyhist(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateField(auto_now_add=True)
	amount = models.CharField(max_length=255)
	status = models.CharField(max_length=255)
	destination = models.CharField(max_length=255)
	def __str__(self):
		return self.amount

