from django.contrib import admin
from .models import Topics


class TopicsAdmin(admin.ModelAdmin):
  list_display =(
    'pk',
    'topic',
  )
  list_editable=(
    'topic',
  )
  list_filter=(
    'topic',
  )


admin.site.register(Topics, TopicsAdmin)