from django.shortcuts import render, redirect
from .models import Tweet
from user_profile.models import Topics
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from user_profile.models import Follow


@login_required 
def send_tweet(request):
    if request.method == 'POST':
        post = request.POST.get('tweet')
        print('tweet : ', post)
        result = Tweet.objects.create(
          user_id=request.user,
          post=post
        )
    if result:
        print('tweet added')
    return redirect('/')


def get_tweet(request, user_id):
    context = dict()
    print('Coming User Id:', user_id)
    user_list = Follow.objects.filter(follower_id = user_id)
    get_id = ""
    for item in user_list:
        print('item id ', item.following_id)
        get_id = item.following_id
    context['last_topics'] = Topics.objects.all().order_by('-pk')[:10]
    context['tweets'] = Tweet.objects.order_by('-pk')
    return render(request, 'index.html', context)



