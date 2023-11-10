from django.conf import settings
from rest_framework import views, status
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer

import subprocess,os



class ExtractAudioView(views.APIView):
    def post(self, request, format=None):
        video_file = request.FILES['file']
        output_filename = video_file.name.split('.')[0] + '.mp3'
        output_path = os.path.join(settings.MEDIA_ROOT, output_filename)

        command = ['ffmpeg', '-i', video_file.temporary_file_path(), '-q:a', '0', '-map', 'a', output_path]
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        

        video_info = Video(user=request.user.username if request.user.is_authenticated else 'Anonymous')
        video_info.save()

        return Response(VideoSerializer(video_info).data, status=status.HTTP_200_OK)
    

class WatermarkVideoView(views.APIView):
    def post(self, request, format=None):
        video_file = request.FILES.get('video')
        watermark_image = request.FILES.get('watermark')
        position = request.data.get('position', 'center')  # Default position


        output_filename = video_file.name.split('.')[0] + '_watermarked.mp4'  # Modified filename
        output_path = os.path.join(settings.MEDIA_ROOT, output_filename)


        command = [
            'ffmpeg', '-i', video_file.temporary_file_path(), '-i', watermark_image.temporary_file_path(),
            '-filter_complex', 'overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2', 
            '-codec:a', 'copy', output_path
        ]
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Save video info to DB
        video_info = Video(user=request.user.username, watermark_image=watermark_image)
        video_info.save()

        return Response(VideoSerializer(video_info).data, status=status.HTTP_200_OK)      

    
