from django.db import models

import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

from django.db.models.signals import post_save

from django.db.models import Q

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,related_name='profile')
    prof_pic = models.ImageField(upload_to = 'them/',default='Profile Pic')
    bio = models.CharField(max_length=300)
    contact = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()

    def create_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    post_save.connect(create_profile,sender=User)
        # user = request.user
        # profile = Profile.objects.filter(user=user).first()
        # return profile

class Post(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'them/',default='Post Image')
    description = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def search_post(cls,name):
        post = cls.objects.filter(name__icontains=name)

        return post

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    comment = models.CharField(max_length=300)

    def save_comment(self):
        self.save()
