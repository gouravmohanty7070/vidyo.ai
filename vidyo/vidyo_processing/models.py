from django.db import models

class Video(models.Model):
    # Basic User Information
    user = models.CharField(max_length=100)

    # Timestamps
    upload_time = models.DateTimeField(auto_now_add=True)
    processed_time = models.DateTimeField(auto_now=True)

    # Processing Type (audio extraction or watermarking)
    processing_type = models.CharField(max_length=20)

    # File names
    original_video_name = models.CharField(max_length=255, blank=True, null=True)
    processed_video_name = models.CharField(max_length=255, blank=True, null=True)

    # Watermarking specific fields
    watermark_image = models.ImageField(upload_to='watermarks/', blank=True, null=True)
    watermark_position = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.user} - {self.processing_type} - {self.original_video_name}"
