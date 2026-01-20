# home/models.py
from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    event_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def remaining_time(self):
        from django.utils import timezone
        delta = self.event_date - timezone.now()
        total_seconds = int(delta.total_seconds())
        if total_seconds < 0:
            return (0, 0, 0)
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return hours, minutes, seconds
