from django.shortcuts import render, redirect
from .models import Tweet
from user_profile.models import Topics, Follow
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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
    # print('\n\n\n ===> Coming User Id:', user_id)
    context = dict()
    user_list = Follow.objects.filter(follower_id = user_id)
    # tweet_list = Tweet.objects.filter(follower_id = user_id)
    # print('\n\n\n ===> User list:', user_list)

    get_id = ""
    for item in user_list:
        print('item id :', item.following_id)
        get_id = item.following_id

    context['last_topics'] = Topics.objects.all().order_by('-pk')[:10]
    context['tweets'] = Tweet.objects.order_by('-pk')
    return render(request, 'index.html', context)
