from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Profile,Image,Follow
from django.contrib.auth.decorators import login_required
from .forms import NewProfForm, NewImageForm

@login_required(login_url='/accounts/login')
def all_images(request):
    profiles = Profile.objects.all()
    date = dt.date.today()
    return render(request,"all-image/home.html", {"date": date,"profiles":profiles,"id":id})

@login_required(login_url='/accounts/login')
def prof(request):
    Profile.user = request.user
    user_id = Profile.user.id
    profile = Profile.objects.filter(id__icontains=user_id)
    images = Image.objects.all()
    print(images)
    return render(request,"all-image/prof.html", {"profile":profile,"images":images,"id":id})

@login_required(login_url='/accounts/login')
def new_img(request):
    current_user = request.user
    # user_id = Profile.user.id
    # current_profile = Profile.objects.filter(id__icontains=user_id)
    if request.method == 'POST':
        form = NewImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user.profile
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
            profile.save()
        return redirect('prof')
    else:
        form = NewProfForm()
    return render(request,'registration/edit_prof.html',{"form": form,"id":id})

@login_required(login_url='/accounts/login/')
def admin(request):
    return render(request)

@login_required(login_url='/accounts/login/')
def follow(request):
    current_user=request.user
    follow=Follow.objects.filter(current_user.id)
    return render(request)
