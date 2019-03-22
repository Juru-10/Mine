from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image
import pyperclip

def all_images(request):
    image=Image.objects.all()
    date=dt.date.today()

    return render(request,"all-image/today-image.html", {"date": date,"image":image})
