from django.db import models

# Create your models here.
class Athist(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateTimeField(auto_now_add=True)
	amount = models.CharField(max_length=25)
	status = models.CharField(max_length=25)
	source = models.CharField(max_length=25)
	destination = models.CharField(max_length=25)
	def __str__(self):
		return self.amount

class Buyhist(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateTimeField(auto_now_add=True)
	amount = models.CharField(max_length=25)
	status = models.CharField(max_length=25)
	destination = models.CharField(max_length=25)
	def __str__(self):
		return self.amount

class Bulkhist(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=25)
	amount = models.CharField(max_length=25)
	status = models.CharField(max_length=25)
	destination = models.CharField(max_length=25)
	def __str__(self):
		return self.amount

