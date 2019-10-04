from django.contrib import admin
from .models import Tweet

class TweetAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user_name',
        'post'
    )

admin.site.register(Tweet, TweetAdmin)