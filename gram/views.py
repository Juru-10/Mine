from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image
import pyperclip

def all_images(request):
    image=Image.objects.all()
    date=dt.date.today()

    return render(request,"all-image/home.html", {"date": date,"image":image})

def prof(request,id):
    user = User.details(id)
    print(image)
    return render(request,"all-image/prof.html", {"user":user,"id":id})
