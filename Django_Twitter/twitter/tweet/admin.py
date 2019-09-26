from .models import Tweet
from django.contrib import admin

class TweetAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user_id',
        'post'
    )

admin.site.register(Tweet, TweetAdmin)