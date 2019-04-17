from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Profile,Post,Comment
from django.contrib.auth.decorators import login_required
from .forms import NewProfForm, NewPostForm, CommentForm

@login_required(login_url='/accounts/login')
def nav(request,id):
    profile = Profile.objects.filter(id=id)
    return render(request,"navbar.html", {"profile":profile,"id":id})

@login_required(login_url='/accounts/login')
def home(request):
    try:
        date = dt.date.today()
        posts = post.objects.all()
    except DoesNotExist:
        raise Http404()
    return render(request,"all_posts/home.html",{"date": date, "posts": posts})

@login_required(login_url='/accounts/login')
def prof(request):
    users =User.objects.all()

    for user in users:
        user=user
        profile = Profile.objects.all()
        posts = post.objects.all()
        print(user)
    return render(request,"all_posts/prof.html",{ "user": user,"profile": profile,"posts": posts})

@login_required(login_url='/accounts/login')
def post(request,id):
    post = post.objects.filter(id__icontains = id)
    return render(request,"all_posts/post",{"post": post})

@login_required(login_url='/accounts/login')
def search(request):
    if 'post' in request.GET and request.GET["post"]:
        title = request.GET.get("post")
        print(title)
        searched_posts = post.search_post(title)
        message = f"{title}"
        return render(request,"all_posts/search.html", {"message": message, "posts": searched_posts})
    else:
        message = "There is no such name"
        return render(request,"all_posts/search.html", {"message": message})

@login_required(login_url='/accounts/login')
def new_prof(request):
    current_user = request.user
    user = User.objects.filter().first()
    if request.method == 'post':
        form = NewProfForm(request.post,request.FILES)
        print(form.errors.as_text())
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            # profile=Profile.objects.update()
            profile.save()
        return redirect('prof')
    else:
        form = NewProfForm()
    return render(request,'registration/new_prof.html',{"form": form,"id":id})

@login_required(login_url='/accounts/login')
def new_post(request):
    current_user=request.user
    profile= Profile.objects.filter(user=current_user.id).first()
    if request.method == 'post':
        form = NewPostForm(request.post,request.FILES)
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile=profile
            post.save()
        return redirect('prof')
    else:
        form = NewPostForm()
    return render(request,'registration/new_post.html',{"form": form,"id":id})

@login_required(login_url='/accounts/login')
def new_comment(request):
    current_user=request.user
    profile= Profile.objects.filter(user=current_user.id).first()
    post= post.objects.filter(profile=profile.id).first()
    if request.method == 'post':
        form = commentForm(request.post,request.FILES)
        # print(form.errors.as_text())
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post=post
            comment.save()
        return redirect('prof')
    else:
        form = commentForm()
    return render(request,'registration/comment.html',{"form": form})

@login_required(login_url='/accounts/login/')
def admin(request):
    return render(request)

@login_required(login_url='/accounts/login/')
def delete(request,id):
    post = post.objects.filter(id=id)
    post.delete()
    return redirect('prof')
