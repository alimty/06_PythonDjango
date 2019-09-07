
from django.contrib import admin
from django.urls import path
from user_profile.views import signup, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('', index)
]
