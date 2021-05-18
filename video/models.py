from django.db import models

# Create your models here.
class Video(models.Model):
    caption = models.CharField(max_length = 100)
    video = models.FileField(upload_to="video/%y")
    def __str__(self):
        return self.caption


class Audio(models.Model):
    title = models.CharField(max_length = 100)
    audio = models.FileField(upload_to="audio/%y")
    def __str__(self):
        return self.title
