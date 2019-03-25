from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    prof_pic = models.ImageField(upload_to = 'gram/',default='SOME STRING')
    bio = HTMLField()
    following = models.BooleanField(default=False)
    followers = models.BooleanField(default=False)
    def __str__(self):
        return self.profile

    @classmethod
    def save_profile(cls):
        profile = cls.objects.create().save()
        return profile

    @classmethod
    def delete_profile(cls):
        profile = cls.objects.delete()
        return profile

    @classmethod
    def edit_profile(cls,id):
        profile = cls.objects.filter(id).update()
        return profile

class Image(models.Model):
    image = models.ImageField(upload_to = 'gram/',default='SOME STRING')
    name = models.CharField(max_length=30)
    caption = HTMLField()
    profile = models.ForeignKey(Profile)
    likes = models.IntegerField()
    comments = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return self.image

    @classmethod
    def save_image(cls):
        image = cls.objects.create()
        image.save()
        return image

    @classmethod
    def delete_image(cls):
        image = cls.objects.delete()

    @classmethod
    def update_caption(cls,id):
        caption = cls.objects.filter(id).update()
        return caption

class Follow(models.Model):
    following = models.ForeignKey(User)
    followers = models.ForeignKey(Profile)
    def __str__(self):
        return self.following
