from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class board(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	slug = models.SlugField()

	def __str__(self):
		return self.title

class post(models.Model):
	title = models.CharField(max_length=236)
	content = models.TextField()
	post_board = models.ForeignKey(board, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	release_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title