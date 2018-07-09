from django.db import models

# Create your models here.
class Smshist(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=25)
	content = models.CharField(max_length=255)
	status = models.CharField(max_length=25)
	destination = models.CharField(max_length=255)
	def __str__(self):
		return self.content
