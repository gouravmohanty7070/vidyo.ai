from django.db import models

class Video(models.Model):
    user = models.CharField(max_length=100)
    upload_time = models.DateTimeField(auto_now_add=True)
    watermark_image = models.ImageField(upload_to='watermarks/', blank=True, null=True)  # Image watermark
    watermark_position = models.CharField(max_length=50, blank=True)  # Position of the watermark
