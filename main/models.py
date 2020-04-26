from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class features(models.Model):
	search=models.CharField(max_length=500)

	def __str__(self):
		return self.search


class Info(models.Model):
	title=models.CharField(max_length=300)
	due_date=models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
	content=models.TextField()
	created=models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.title