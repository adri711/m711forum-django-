from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='forum-home'),
	path('forumdisplay/<slug:boardslug>/', views.forumdisplay, name='forumdisplay'),
	path('<slug:boardslug>/<int:postid>/', views.postdisplay, name='postdisplay')
]