from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    user_id = models.ForeignKey(
      User, on_delete=models.CASCADE
    )
    post = models.CharField(max_length=240)
    like = models.PositiveIntegerField(default=0)
    retweet = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)