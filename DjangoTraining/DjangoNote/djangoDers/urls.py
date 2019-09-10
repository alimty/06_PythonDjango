
from django.contrib import admin
from django.urls import path
from note.views import index, show_notes, todo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('notes/', show_notes, name='show_notes'),
    path('todo/', todo, name='todo'),
]
