from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render_to_response

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

#from turbomansion.apps import TurboMansion
import pychromecast as pycc

def home(request):
    name = ""

    if (request.user.is_authenticated):
        name = request.user.username

    return render_to_response("turbomansion/home.html", {"username" : name})

def logmeout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def profile(request):
    name = "no name"

    if (request.user.is_authenticated):
        name = request.user.username

    return render_to_response("turbomansion/profile.html", {"username": name})


@login_required
def cast(request):
    casts = pycc.get_chromecasts_as_dict().keys()

    return render_to_response("turbomansion/cast.html", {"casts" : casts})

from pychromecast.controllers.youtube import YouTubeController
def playYoutubeVideo(request, cast_name, video_id):
    yt = YouTubeController()
    cast = pycc.get_chromecast(friendly_name=cast_name)

    cast.register_handler(yt)
    yt.play_video(video_id)
    return HttpResponse("Playing {} on {}".format(video_id, cast_name))
    

def stopCast(request, cast_name):
    cast = pycc.get_chromecast(friendly_name=cast_name)
    cast.quit_app()
    return HttpResponse(cast_name)

