from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from board.models import post, reply

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user_created = form.save()
                username = form.cleaned_data.get('username')
                new_profile = profile(user=user_created)
                new_profile.save()
                messages.success(request, f"Your account has been successfuly created with the following username: {username}")
                return redirect("signin")
        else:
            form = UserRegistrationForm()
        return render(request, 'users/signup.html', {'signup_form': form})
    else:
        return redirect('forum-home')

@login_required
def profileshow(request, spec_user_pk):
    
    context = {'title': 'profile'}
    spec_user = User.objects.all().filter(pk=spec_user_pk)[0]
    context = {
        'spec_user': spec_user,
        'profile': profile.objects.all().filter(user=spec_user).first(),
        'statistics': {
            'postcount': len(post.objects.all().filter(author=spec_user)),
            'replies': len(reply.objects.all().filter(author=spec_user))
        }
    }

    return render(request, 'users/profile.html', context)

@login_required
def settings(request):
    pass