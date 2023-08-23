from django.db import models
from datetime import datetime

class song(models.Model):
    song_name=models.CharField(max_length=100)
    artist=models.CharField(max_length=30)
    Duration_time=models.FloatField()
    song=models.FileField(upload_to='musics/')
    date=models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self) -> str:
        return self.song_name
    
