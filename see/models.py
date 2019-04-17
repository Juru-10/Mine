from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# from comment.models import CommentModel

class Follow(models.Model):
    following = models.ForeignKey(User,related_name='following')
    followers = models.ForeignKey(User,related_name='followers')

    def __str__(self):
        return self.following

    def save_follow(self):
        self.save()

    @classmethod
    def save_f(cls):
        follow = cls.objects.create().save()
        return follow

class Profile(models.Model):
    user = models.OneToOneField(User, null=True)
    prof_pic =  models.ImageField(upload_to = 'gram/')
    bio = models.CharField(max_length=100)
    follow = models.ManyToManyField(Follow)

    def __str__(self):
        return self.user.username

    @classmethod
    def save_profile(cls):
        profile = cls.objects.save()
        return profile

    @classmethod
    def delete_profile(cls):
        profile = cls.objects.delete()
        return profile

    @classmethod
    def edit_profile(cls,id):
        profile = cls.objects.filter(id).update(id)
        return profile

class Comment(models.Model):
    comment = models.CharField(max_length=100,null=True)
    

# class Like(models.Model):
#     like = models.BooleanField(default=False)

class Image(models.Model):
    image = models.ImageField(upload_to = 'gram/',default='SOME STRING')
    name = models.CharField(max_length=30)
    caption = HTMLField()
    profile = models.ForeignKey(Profile, null=True)
    # likes = models.ForeignKey(Like, null=True)
    comments = models.ForeignKey(Comment, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

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

    @classmethod
    def count_commments(cls):
        return cls.comments.count()

    @classmethod
    def all_comments(cls):
        return cls.comments.filter(user_id=user_id)
