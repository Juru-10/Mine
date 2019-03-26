from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Profile,Image,Follow
from django.contrib.auth.decorators import login_required
from .forms import NewProfForm, NewImageForm

@login_required(login_url='/accounts/login')
def all_images(request):
    image = Image.objects.all()
    date = dt.date.today()
    return render(request,"all-image/home.html", {"date": date,"image":image})

@login_required(login_url='/accounts/login')
def prof(request):
    current_user = request.user
    profile = Profile.objects.filter()
    # print(profile)
    return render(request,"all-image/prof.html", {"profile":profile,"id":id})

@login_required(login_url='/accounts/login')
def new_img(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            # image.profile = current_user
            print(image.image)
            image.save()
        return redirect('prof')
    else:
        form = NewImageForm()
    return render(request,'registration/new_img.html',{"form": form})

@login_required(login_url='/accounts/login')
def edit_prof(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfForm(request.POST,request.FILES)
        print(form.errors.as_text())

        if form.is_valid():
            # print(form.is_valid())
            profile = form.save(commit=False)
            profile.user = current_user
            print(profile.prof_pic)
            # profile.edit_profile(id)
            profile.save_profile()
        return redirect('prof')
    else:
        form = NewProfForm()
    return render(request,'registration/edit_prof.html',{"form": form,"id":id})

@login_required(login_url='/accounts/login/')
def admin(request):
    return render(request)
