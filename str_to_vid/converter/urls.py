from django.urls import path

from converter.apps import ConverterConfig
from converter.views import download_video, index, VideoListView

app_name = ConverterConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('download/<int:pk>/', download_video, name='download_video'),
    path('videos/', VideoListView.as_view(), name='videos'),
]
