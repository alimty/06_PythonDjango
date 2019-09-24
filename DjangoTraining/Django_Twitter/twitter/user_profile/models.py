from django.db import models


class Topics(models.Model):
    topic = models.CharField(max_length=300, blank=False)


class Follow(models.Model):
<<<<<<< HEAD
    follower_id = models.CharField(max_length=100)
    following_id = models.CharField(max_length=100)
=======
    follow_id = models.CharField(max_length=100)
    following_id = models.CharField(max_length=100)
>>>>>>> 0533f8d1619755e730830e7626d67534ca7be334
