from django.db import models

# Create your models here.

class Fwno(models.Model):
	id = models.AutoField(primary_key=True)
	num = models.CharField(max_length=13)
	def __str__(self):
		return self.num