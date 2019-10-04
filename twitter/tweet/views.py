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
    context = dict()
    context['last_topics'] = Topics.objects.all().order_by('-pk')[:10]
    user_list = Follow.objects.filter(follower_id=user_id)
    tweet_list = list()
    for item in user_list:
        tweet_list.append(Tweet.objects.filter(user_name=item.following_id).order_by('-pk'))
    tweets = list()
    for i in tweet_list:
        for j in i:
            # print("user post :", j.post,  " user name: ", j.user_name)
            tweets.append(j)
    sorted(tweets, key=lambda x: x.created_date),
    tweets.sort(key=lambda x: x.created_date, reverse=True)
    context['tweets'] = tweets
    return render(request, 'index.html', context)


"""
JSON
context = {
    'tweets' : [
        user_id-tweet1,
        user_id-tweet2,
        user_id-tweet3,
        ...
    ]
    }


    #here user catching yourself as a follower from follow table. Which means I following bunch of people with number of tweets. lets say I'm follower of 3 person.

    # I'm creating tweet list that comes from person that I followed which will be visible in my main screen.
    for item in user_list:
    # here item is group of tweets because each user can have multiple tweets

"""
