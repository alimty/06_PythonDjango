from django.contrib import admin
from .models import Topics, Follow


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


class FollowAdmin(admin.ModelAdmin):
    list_display = (
<<<<<<< HEAD
      'pk',
      'follow_id',
      'following_id'
    )


admin.site.register(Follow, FollowAdmin)
admin.site.register(Topics, TopicsAdmin)
=======
        'pk',
        'follow_id',
        'following_id'
    )


admin.site.register(Topics, TopicsAdmin)
admin.site.register(Follow, FollowAdmin)
>>>>>>> 0533f8d1619755e730830e7626d67534ca7be334
