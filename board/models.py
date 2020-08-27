from django.db import models
from django.contrib.auth.models import User

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
	release_date = models.DateTimeField(auto_now_add=True)
	views = models.IntegerField(default=0)
	last_activity = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class reply(models.Model):

	content = models.TextField()
	reply_to = models.ForeignKey(post, on_delete=models.CASCADE)
	release_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return 'reply to -> ' + self.reply_to.title + ' by ' +  self.author.username