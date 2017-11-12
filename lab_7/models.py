from django.db import models

class Friend(models.Model):
    friend_name = models.CharField(max_length=400)
    npm = models.CharField(max_length=250)
    added_at = models.DateField(auto_now_add=True)