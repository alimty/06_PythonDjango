from django.contrib import admin
from .models import Person, Book, Todo


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


class TodoAdmin(admin.ModelAdmin):
  list_display = (
        'id',
        'todouser',
        'todotask',
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Todo, TodoAdmin)
