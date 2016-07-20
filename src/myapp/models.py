from __future__ import unicode_literals

from django.db import models

# Create your models here.

class NewsSignUp(models.Model):
	nombre = models.CharField(max_length=100)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self): #Python3 __str__
		return self.nombre