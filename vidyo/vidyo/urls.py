from django.contrib import admin
from django.urls import path
from vidyo_processing.views import ExtractAudioView, WatermarkVideoView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('extract-audio/', ExtractAudioView.as_view()),
    path('watermark-video/', WatermarkVideoView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
