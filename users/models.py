from django.db import models
from django.contrib.auth.models import User


class member(User):
	biography = models.TextField(default='')
	location = models.CharField(max_length=52, default='')
	avatar = models.ImageField(default='default.jpg', upload_to='profile_pics')
	def __str__(self):
		return self.username