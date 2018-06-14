from django.db import models

# Create your models here.
class Smshist(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateField(auto_now_add=True)
	content = models.CharField(max_length=255)
	status = models.CharField(max_length=255)
	destination = models.CharField(max_length=255)
	def __str__(self):
		return self.content
