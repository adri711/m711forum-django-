from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f"Your account has been successfuly created with the following username: {username}")
                return redirect("signin")
        else:
            form = UserRegistrationForm()
        return render(request, 'users/signup.html', {'signup_form': form})
    else:
        return redirect('forum-home')

@login_required
def profile(request):
    return render(request, 'users/profile.html')