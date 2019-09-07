from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



def signup(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    if User.objects.filter(email=email).count():
      print('email adresi mevcut')
      return redirect('/')
    if User.objects.filter(username=username).count():
      print('username mevcut')
      return redirect('/')
    User.objects.create_user(
      username=username,
      email=email,
      password=password
    )
    user = authenticate(
      username = username,
      password = password
    )
    if user is not None:
      print(user)
      login(request, user)
      return redirect('/')
  return render (request, 'signup.html')


def index(request):
    return render(request, 'index.html')