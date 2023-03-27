from django.db import models


class Post(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='post', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=200, blank=True, default='')
