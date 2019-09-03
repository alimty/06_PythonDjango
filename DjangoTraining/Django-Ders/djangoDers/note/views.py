from django.shortcuts import render
from .models import Person


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