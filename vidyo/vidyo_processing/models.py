from django.db import models

class Video(models.Model):
    user = models.CharField(max_length=100)
    upload_time = models.DateTimeField(auto_now_add=True)
