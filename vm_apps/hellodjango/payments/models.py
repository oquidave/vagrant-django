from django.db import models

# Create your models here.
class Payhist(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=25)
	amount = models.CharField(max_length=25)
	status = models.CharField(max_length=25)
	destination = models.CharField(max_length=25)
	def __str__(self):
		return self.amount
