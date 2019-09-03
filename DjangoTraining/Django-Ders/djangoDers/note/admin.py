from django.contrib import admin
from .models import Person, Book


class PersonAdmin (admin.ModelAdmin):
  list_display = (
      'pk',
      'username',
      'title',
      'note',
    ) 
  list_editable = (
    'note',
  )

  list_filter = ('title',)

admin.site.register(Person, PersonAdmin)


class BookAdmin (admin.ModelAdmin):
  list_display = (
    'id',
    'book_name',
    'author',
    'stock_info',
    'add_date',

  )
  list_editable = (
    'stock_info',
  )
  list_filter = (
    'author',
  )

admin.site.register(Book, BookAdmin)