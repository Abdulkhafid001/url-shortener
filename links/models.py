from django.db import models
from django.utils import timezone
from datetime import timedelta


def default_expiry(days=14):
    return timezone.now() + timedelta(days)


class URL(models.Model):
    long_url = models.TextField(name='long_url', unique=True, blank=False)
    short_code = models.CharField(name='short_code', unique=True, blank=False)
    expiry = models.DateTimeField(default=default_expiry())
    custom_alias = models.CharField(name='custom_alias')
    clicks = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.short_code
