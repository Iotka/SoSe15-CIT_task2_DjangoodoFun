from django.db import models
from django.core.urlresolvers import reverse

# Create your models here

class Task(models.Model):
	title=models.CharField(max_length=80)
	description=models.CharField(max_length=200)
	status=models.IntegerField(default=0)
	deadline=models.DateField()
	
	def __str__(self):
		return self.title
	def color(self):
		return "warning"
	def get_absolute_url(self):
		return "/%i" %self.id

