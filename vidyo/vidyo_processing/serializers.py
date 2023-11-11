from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            'user', 
            'processing_type', 
            'original_video_name', 
            'processed_video_name', 
            'watermark_image', 
            'watermark_position'
        ]
        read_only_fields = ['upload_time', 'processed_time']
