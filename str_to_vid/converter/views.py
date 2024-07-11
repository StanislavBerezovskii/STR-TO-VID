from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from converter.models import Video
from helpers.helpers import create_video_from_message, conversion_to_h264


@csrf_exempt
def index(request):
    # catches POST requests
    if request.method == 'POST':
        message = str(request.POST.get('message', ''))
        output = create_video_from_message(message)
        # conversion_to_h264(f'media/{output["path"]}')
        new_video = Video(title=output['title'], message=message, video=output['path'])
        new_video.save()
        context = {'object': new_video}
        return render(request, 'converter/index.html', context)
    # otherwise just shows page
    else:
        context = {}
        return render(request, 'converter/index.html', context)


def download_video(request, pk):
    video = Video.objects.get(pk=pk)
    response = HttpResponse(video.video, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{video.video.name}"'
    return response


class VideoListView(ListView):
    model = Video

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        print(queryset)
        return queryset
