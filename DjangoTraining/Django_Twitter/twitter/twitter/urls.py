
from django.urls import path
from django.contrib import admin
from django.urls import path
from user_profile.views import signup, index, user_login, user_logout, follow
from tweet.views import send_tweet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup),
    path('', index),
    path('login/', user_login),
    path('logout/', user_logout),
    path('tweet/tweet-post/', send_tweet),
    path('follow/<int:following_id>', follow)
]
