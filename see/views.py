from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Profile,Image,Follow,Comment
from django.contrib.auth.decorators import login_required
from .forms import NewProfForm, NewImageForm, CommentForm

@login_required(login_url='/accounts/login')
def nav(request,id):
    profile = Profile.objects.filter(id=id)
    return render(request,"navbar.html", {"profile":profile,"id":id})

@login_required(login_url='/accounts/login')
def all_images(request):
    profiles = Profile.objects.all()
    image = Image.objects.all()
    date = dt.date.today()
    return render(request,"all-image/home.html", {"date": date,"profiles":profiles,"image":image})

@login_required(login_url='/accounts/login')
def prof(request):
    current_user = request.user
    print(current_user.id)
    profile = Profile.objects.filter(id=2*current_user.id+5)
    print(Profile.user)
    Profile.user = request.user
    user_id = Profile.user.id
    profile = Image.profile
    images = Image.objects.all()
    # print(images)
    return render(request,"all-image/prof.html", {"profile":profile,"images":images,"id":id})

@login_required(login_url='/accounts/login')
def new_img(request):
    current_user = request.user

    if request.method == 'POST':
        form = NewImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            # image.profile = Profile.id
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
    # Follow.following+=1
    following=Follow.following
    Profile.follow=following
    return render(request,"all-image/home.html")

@login_required(login_url='/accounts/login/')
def delete(request,id):
    image = Image.objects.filter(id=id)
    image.delete()
    return redirect('prof')

@login_required(login_url='/accounts/login/')
def comment(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST,request.FILES)
        print(form.errors.as_text())

        if form.is_valid():
            # print(form.is_valid())
            comment = form.save(commit=False)
            # comments.user = current_user
            # print(profile.prof_pic)
            # profile.edit_profile(id)
            comment.save()
        return redirect('prof')
    else:
        form = CommentForm()
    return render(request,'registration/comment.html',{"form": form,"id":id})

# @login_required(login_url='/accounts/login/')
# def like(request):
#     like = Like.like.count()
#     like.save()
#     return redirect('prof')
