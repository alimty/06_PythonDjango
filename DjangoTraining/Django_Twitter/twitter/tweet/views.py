from django.shortcuts import render, redirect
from .models import Tweet
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 

@login_required 
def send_tweet(request):
  if request.method == 'POST':
    post = request.POST.get('tweet')
    print('tweet : ', post)
    result = Tweet.objects.create(
      user_id = request.user,
      post = post
    )
    if result:
      print('tweet added')
  return redirect('/')

def get_tweet(request):
  context= dict()
  context['tweets']= Tweet.objects.order_by('-pk')
  return render(request, 'index.html', context)
      


