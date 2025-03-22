from django.shortcuts import render
from django.conf import settings
import os, json, requests
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="/full/path/to/your/mistral-model",
    device=0
)

API_KEY = settings.ELEVENLABS_API_KEY

HEADERS = {"xi-api-key": API_KEY, "Content-Type": "application/json"}

@csrf_exempt
def get_voices(request):
    resp = requests.get("https://api.elevenlabs.io/v1/voices", headers=HEADERS)
    return JsonResponse(resp.json())                              # return list of voices

@csrf_exempt
def tts(request):
    body = json.loads(request.body)
    payload = {"text": body["text"]}
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{body['voice_id']}"
    resp = requests.post(url, headers=HEADERS, json=payload)
    return HttpResponse(resp.content, content_type="audio/mpeg")  # return MP3 bytes

def index(request):
    return render(request, "app/index.html")



def generate(request):
    prompt = request.GET.get("prompt", "")               # grab ?prompt=... from URL
    result = generator(prompt, max_new_tokens=100)[0]    # generate up to 100 tokens
    return JsonResponse({"text": result["generated_text"]})  

