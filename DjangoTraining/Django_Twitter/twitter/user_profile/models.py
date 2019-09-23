from django.db import models


class Topics(models.Model):
    topic = models.CharField(max_length=300, blank=False)


class Follow(models.Model):
    follow_id = models.CharField(max_length=100)
    following_id = models.CharField(max_length=100)