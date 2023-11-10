from moviepy.editor import VideoFileClip
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