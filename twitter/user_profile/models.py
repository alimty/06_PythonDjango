from django.db import models
from django.contrib.auth.models import User


class Topics(models.Model):
    topic = models.CharField(max_length=300, blank=False)


class Follow(models.Model):
    follower_id = models.CharField(max_length=200)
    following_id = models.ForeignKey(
        User, on_delete=models.CASCADE
    )