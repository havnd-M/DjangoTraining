
from django.http import HttpResponse, FileResponse, JsonResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.


def Home(request):
    time = datetime.now()
    return render(request, 'index.html', {'name': '', 'created': time})


def what_is_myip(request):
    return JsonResponse({'ip': '123.123.123.123'})


def home(request):
    return HttpResponse('Hello Django')


def about(request):
    return HttpResponse('<h1>ne ogrenmek istiyorsun?</h1>')


def connection(request):
    return HttpResponse('merhaba dunya')
