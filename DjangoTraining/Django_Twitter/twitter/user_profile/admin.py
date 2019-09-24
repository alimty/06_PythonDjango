from django.contrib import admin
from .models import Topics, Follow


class TopicsAdmin(admin.ModelAdmin):
    list_display =(
      'pk',
      'topic',
    )
    list_editable = (
      'topic',
    )
    list_filter = (
      'topic',
    )


class FollowAdmin(admin.ModelAdmin):
    list_display = (
      'pk',
      'follow_id',
      'following_id'
    )


admin.site.register(Topics, TopicsAdmin)
admin.site.register(Follow, FollowAdmin)
