from django.db import models


class Topics(models.Model):
    topic = models.CharField(max_length=300, blank=False)


class Follow(models.Model):
    follower_id = models.CharField(max_length=100)
    following_id = models.CharField(max_length=100)
    follow_id = models.CharField(max_length=100)
    following_id = models.CharField(max_length=100)
