from django.shortcuts import render
from .models import Video
from .models import Audio

# Create your views here.
def index(request):
    video = Video.objects.all()
    audio = Audio.objects.all()
    return render(request, 'index.html', {"video":video, "audio":audio})
