from django.test import TestCase

from .models import User,Profile,Image,Follow
import datetime as dt

class ProfileTest(TestCase):
    def setUp(self):
        self.prof = Profile(prof_pic =self.prof_pic, bio = self.bio)
        self.prof.save_profile()

        self.prof_pic = Profile(prof_pic = 'Test Image')
        self.prof_pic.save()

        self.bio = Profile(bio = 'Test')
        self.bio.save()

    def test_save_method(self):
        self.prof.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

class FollowTest(TestCase):
    def setUp(self):
        self.follow = Follow(following = self.following,followers = self.followers)
        self.follow.save_follow()

        self.following = Follow(following = 1)
        self.following.save()

        self.followers = Follow(followers = 1)
        self.followers.save()

    def test_save_method(self):
        self.follow.save_follow()
        follows = Follow.objects.all()
        self.assertTrue(len(follows) > 0)

class ImageTestClass(TestCase):
    def setUp(self):
        self.new_img = Image(name = 'Test Image',caption = 'This is a random test Post',profile=self.profile)
        self.new_img.save_image()

        self.name= Image(name='name')
        self.name.save()

        self.profile= Image(profile='profile_id')
        self.profile.save()

        self.caption= Image(caption='caption')
        self.caption.save()
        self.caption.update()

    def tearDown(self):
        Profile.objects.all().delete()
        Image.objects.all().delete()
        Follow.objects.all().delete()

    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_update_caption(self,id=2):
        self.update_caption(caption='caption')
        caption = Image.caption.filter(id=2)
