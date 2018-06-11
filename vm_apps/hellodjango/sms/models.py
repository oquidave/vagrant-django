from django.db import models

# Create your models here.
class smshist(models.Model):
	date = models.CharField()
	content = models.CharField()
	status = models.CharField()
	destination = models.CharField()

