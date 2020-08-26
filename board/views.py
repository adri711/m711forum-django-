from django.shortcuts import render
from . models import board, post

def home(request):
	context = { 'boards': board.objects.all(), 'title': 'Home page' }
	return render(request, "board/home.html", context)

def alter_posts(posts_list):
	for each_post in posts_list:
		each_post.content = each_post.content[:50] + '...'

def forumdisplay(request, boardslug=None):
	context = { 'board': None }
	if boardslug:
		context['board'] = board.objects.all().filter(slug=boardslug).first()
		if context['board']:
			context['posts'] = post.objects.all().filter(post_board=context['board'])
			alter_posts(context['posts'])

	return render(request, "board/forumdisplay.html", context)

def postdisplay(request, boardslug, postid):
	try:
		requested_post = post.objects.all().filter(pk=postid).first()
	except:
		requested_post = None
	context = {'post': requested_post}
	return render(request, "board/postdisplay.html", context)