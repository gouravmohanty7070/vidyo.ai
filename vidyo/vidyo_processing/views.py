from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip
from django.conf import settings
from rest_framework import views, status
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer


class ExtractAudioView(views.APIView):
    def post(self, request, format=None):
        # Extract audio from video
        video_file = request.FILES['file']
        video = VideoFileClip(video_file.temporary_file_path())
        audio = video.audio

        # Define the path to save the audio file (for a Mac)
        audio_file = "/Users/gouravmohanty/Desktop/audio.mp3"  # Update with your path

        audio.write_audiofile(audio_file)

        # Save video info to DB
        video_info = Video(user=request.user.username)
        video_info.save()

        return Response(VideoSerializer(video_info).data, status=status.HTTP_200_OK)
    

class WatermarkVideoView(views.APIView):
    def post(self, request, format=None):
        video_file = request.FILES.get('video')
        watermark_image = request.FILES.get('watermark')
        position = request.data.get('position', 'center')  # Default position

        if not video_file or not watermark_image:
            return Response({"message": "Video and watermark image are required."}, 
                            status=status.HTTP_400_BAD_REQUEST)

        video_clip = VideoFileClip(video_file.temporary_file_path())
        watermark_clip = ImageClip(watermark_image.temporary_file_path(), duration=video_clip.duration)

        # Positioning the watermark
        watermark_clip = watermark_clip.set_position(position)

        # Overlay watermark on video
        final_clip = CompositeVideoClip([video_clip, watermark_clip])
        output_path = f"/Users/gouravmohanty/Desktop/{video_file.name}"
        final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

        # Save video info to DB
        video_info = Video(user=request.user.username, watermark_image=watermark_image)
        video_info.save()

        return Response(VideoSerializer(video_info).data, status=status.HTTP_200_OK)
