from django.db import models


class Topics(models.Model):
    topic = models.CharField(max_length=300, blank=False)
