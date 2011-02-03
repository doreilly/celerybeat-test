from django.db import models

class CeleryBeatLog(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    
    class Meta:
        get_latest_by = ('timestamp',)
    
