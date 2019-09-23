from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from tweet.views import get_tweet
from .models import Topics, Follow


def signup(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    if User.objects.filter(email=email).count():
      print('email adresi mevcut')
      return redirect('/signup')
    if User.objects.filter(username=username).count():
      print('username mevcut')
      return redirect('/signup')
    User.objects.create_user(
      username=username,
      email=email,
      password=password
    )
    user = authenticate(
      username=username,
      password=password
    )
    if user is not None:
      print(user)
      login(request, user)
      return redirect('/')
  return render (request, 'signup.html')


# def show_last_topics(request):
#     context = dict()
#     context['last_topics'] = Topics.objects.order_by('-pk')
#     return render(request, 'index.html', context)


def index(request):
    if request.user.is_authenticated:
        return get_tweet(request, request.user.id)
    return redirect('/login')


def user_login(request):
    if request.method =='POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      if username and password is not None:
        user = authenticate(
          username=username,
          password=password
        )
        print('id:', user.id)
        if user is not None:
          login(request, user)
          return redirect('/')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('/')


def follow(request, following_id):
    if request.method == 'GET':
        print ('user ID: ', request.user.id, 'folowing ID', following_id)
        result = Follow.objects.create(
          follow_id=request.user.id,
          following_id=following_id
        )
        if result:
          print('Follow is successful')
        else:
          print('Sikinti var')
    return redirect('/')