from django.shortcuts import render, redirect
from .models import Tweet
from user_profile.models import Topics, Follow
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
<<<<<<< HEAD
    context = dict()
    print('Coming User Id:', user_id)
    user_list = Follow.objects.filter(follower_id = user_id)
    get_id = ""
    for item in user_list:
        print('item id ', item.following_id)
        get_id = item.following_id
    context['last_topics'] = Topics.objects.all().order_by('-pk')[:10]
    context['tweets'] = Tweet.objects.order_by('-pk')
=======
    context = dict() #context = {}
    print('Gelen user Id:', user_id)
    user_list = Follow.objects.filter(follow_id = user_id)
    get_id = ""
    for item in user_list:
      print('item id: ', item.following_id)
      get_id = item.following_id
    # context['last_topics'] = Topics.objects.order_by('-pk')
    context['last_topics'] = Topics.objects.all().order_by('-pk')[:10]
    # context = dict()
    context['tweets'] = Tweet.objects.filter(user_id=get_id).order_by('-pk')
>>>>>>> 0533f8d1619755e730830e7626d67534ca7be334
    return render(request, 'index.html', context)

