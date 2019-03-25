from django.test import TestCase

from .models import User,Profile,Image
import datetime as dt

class ProfileTest(TestCase):
    def setUp():
        self.assumpta = Profile(user = 'Assumpta', prof_pic =self.prof_pic, bio = self.bio)
        self.assumpta.save_profile()

        self.prof_pic = Profile(prof_pic = 'Test Image')
        self.prof_pic.save()

        self.bio = Profile(bio = 'Test')
        self.bio.save()

    def test_save_method(self):
        self.james.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

class FollowTest(TestCase):
    def setUp():
        self.follow = Follow(following = self.following,followers = self.followers)
        self.follow.save_follow()

        self.following = Follow(following = 1)
        self.following.save()

        self.followers = Follow(followers = 1)
        self.followers.save()

    def test_save_method(self):
        self.follow.save_follows()
        follows = Follow.objects.all()
        self.assertTrue(len(follows) > 0)

class ImageTestClass(TestCase):
    def setUp(self):
        self.new_img = Image(name = 'Test Image',caption = 'This is a random test Post',profile = self.assumpta,likes = self.new_l,comments = self.new_c)
        self.new_img.save_image()

        self.name= Image(name='name')
        self.name.save()

        self.caption= Image(caption='caption')
        self.caption.save()
        self.caption.update()

        self.profile= Profile(id=1)
        self.profile=save()

        self.new_l = Like(like = 1)
        self.new_l.save()

        self.new_c = Comment(comment = 'comment')
        self.new_c.save()

    def tearDown(self):
        Profile.objects.all().delete()
        Image.objects.all().delete()
        Follow.objects.all().delete()

    def test_save_method(self):
        self.james.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
