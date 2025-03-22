from django.urls import path
from .views import index, get_voices, tts, generate

urlpatterns = [ 
    path("", index, name="index"),
    path("voices/", get_voices),
    path("tts/", tts),
    path("generate/", generate),
]