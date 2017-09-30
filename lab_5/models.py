from django.db import models

class Todo(models.Model):
	title = models.CharField(max_length=27)
	description = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)