from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Profile,Image,Follow
from django.contrib.auth.decorators import login_required
from .forms import NewProfForm, NewImageForm

@login_required(login_url='/accounts/login')
def all_images(request):
    image=Image.objects.all()
    date=dt.date.today()

    return render(request,"all-image/home.html", {"date": date,"image":image})

@login_required(login_url='/accounts/login')
def prof(request,id):
    user = User.details(id)
    print(image)
    return render(request,"all-image/prof.html", {"user":user,"id":id})

@login_required(login_url='/accounts/login')
def new_img(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('all_images')
    else:
        form = NewImageForm()
    return render(request,'new_img.html',{"form": form})

def signup(request):
    if request.method == 'POST':
        form = NewProfForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('/accounts/login/?next=/')
    else:
        form = NewProfForm()
    return render(request,'registration/registration_form.html',{"form": form})
