from django.db import models

# Create your models here.
class Contact(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateTimeField(auto_now_add=True)
	contact = models.CharField(max_length=13)
	def __str__(self):
		return self.contact
