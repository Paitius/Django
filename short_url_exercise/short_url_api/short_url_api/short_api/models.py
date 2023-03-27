from django.db import models
from django.core.validators import URLValidator


class Url(models.Model):
    long = models.CharField(max_length=5000)
    short = models.CharField(max_length=40)

    def clean(self, *args, **kwargs):
        validator = URLValidator()
        validator(self.long)
        super().clean(*args, **kwargs)
