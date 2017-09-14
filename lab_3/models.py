from django.db import models

# Create your models here.
class Diary(models.Model):
	date = models.DateTimeField()
	activity = models.TextField(max_length=60)