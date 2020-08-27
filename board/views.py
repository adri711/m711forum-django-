from django.shortcuts import render, redirect
from . models import board, post, reply
from .forms import*
from django.utils import timezone

def home(request):

	context = { 'boards': board.objects.all(), 'title': 'Home page' }
	[setattr(b, 'latest_posts', post.objects.all().filter(post_board=b).order_by('last_activity')[:3]) for b in context['boards']]
	
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
			context['posts'] = context['posts'].order_by('-last_activity')
			[setattr(eachpost, 'reply_count', len(reply.objects.all().filter(reply_to=eachpost))) for eachpost in context['posts']]
			alter_posts(context['posts'])
		else:
			pass
	else:
		pass

	return render(request, "board/forumdisplay.html", context)

def postdisplay(request, boardslug, postid):
	
	requested_post = post.objects.all().filter(pk=postid).first()
	replies = reply.objects.all().filter(reply_to=requested_post)
	context = { 'post': requested_post, 'replies': replies }

	if request.user.is_authenticated:
		requested_post.views+=1
		requested_post.save()
		context['form'] = ReplyForm(request.POST)
		if context['form'].is_valid():
			obj_pointer = post.objects.all().filter(pk=postid).first()
			context['form'].clean()
			new_reply = reply(content=request.POST['reply_content'], author=request.user, reply_to=obj_pointer)
			new_reply.save()
			obj_pointer.last_activity = timezone.now()
			obj_pointer.save()
			return redirect('forum-home')

	return render(request, "board/postdisplay.html", context)

def createpost(request, boardslug):
	if request.user.is_authenticated:
		board_target = board.objects.all().filter(slug=boardslug).first()
		if board_target:
			form = PostCreationForm(request.POST)
			context = { 'post_create_form': form }
			if form.is_valid():
				new_post = post(title=request.POST['title'], content=request.POST['content'],post_board=board.objects.all().filter(slug=boardslug).first(), author=request.user)
				new_post.save()
				return redirect("forum-home")
			return render(request, "board/createpost.html", context)
		else:
			context = {'error': 'ERROR: 404'}
			return render(request, "board/createpost.html", context)
	else:
		return redirect('signin')