from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['user', 'upload_time', 'watermark_image', 'watermark_position']

