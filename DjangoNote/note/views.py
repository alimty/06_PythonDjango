from django.shortcuts import render, redirect
from .models import Person, Todo


def index(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    title = request.POST.get('title')
    note = request.POST.get('note')
    result = Person.objects.create(
      username=username,
      title=title,
      note=note, 
    )
    if result:
      print('Kayit basarili')
    else:
      print('Kayit yapilmadi')

  return render(request, 'index.html')


def show_notes(request):
    context = dict()
    context ['notes'] = Person.objects.all().order_by('-pk')
    return render(request, 'notes.html', context)

def todo(request):
  if request.method == 'POST':
    todouser = request.POST.get('todouser')
    if todouser is None:
      print ('No user')
      return redirect('/')
    todotask = request.POST.get('todotask')
    result = Todo.objects.create(
      todouser=todouser,
      todotask=todotask
    )
    if result:
      print('Todo Saved')
    else:
      print('Not Saved')
  return render(request, 'todo.html')
