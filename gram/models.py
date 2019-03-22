from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length = 30)
    username = models.CharField(max_length = 30)
    email = models.EmailField()
    password = models.CharField(min_legth = 8)
    prof_pic = models.ImageField(upload_to = 'image/',default='SOME STRING')
    posts = models.ForeignKey(Image)
    following = models.ForeignKey(Follower)
    followers = models.IntegerField()

    def __str__(self):
        return self.first_name

    def save_user(self):
        self.save()

    def display_users():
        User.objects.all()

    def update_user(self):
        User.objects.filter(self).update(self)

    class Meta:
        ordering = ['first_name']

class Follower(models.Model):
    follow = models.BooleanField()
    def __str__(self):
        return self.follow

    def save_follow(self):
        self.save()

    def display_follows():
        Follower.objects.all()

    def update_follow(self):
        Follower.objects.filter(self).update(self)

class Comment(models.Model):
    comment = models.CharField(max_length =200)
    def __str__(self):
        return self.comment

    def save_user(self):
        self.save()

    def display_comments():
        Comment.objects.all()

    def update_comment(self):
        Comment.objects.filter(self).update(self)


class Like(models.Model):
    like = models.BooleanField()
    def __str__(self):
        return self.like

    def save_like(self):
        self.save()

    def display_likes():
        Like.objects.all()

    def update_like(self):
        Like.objects.filter(self).update(self)


class Image(models.Model):
    image = models.ImageField(upload_to = 'image/',default='SOME STRING')
    user = models.ForeignKey(User)
    comment = models.ForeignKey(Comment)
    like = models.ForeignKey(Like)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
