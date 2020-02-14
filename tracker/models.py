from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class League(models.Model):
	player = models.ForeignKey(User, on_delete=models.CASCADE)
	leage_type = models.CharField(max_length=100)
	my_deck_name = models.CharField(max_length=100)
	record = models.IntegerField()
	date = models.DateTimeField(default=timezone.now)