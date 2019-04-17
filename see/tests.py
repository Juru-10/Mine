from django.test import TestCase

from .models import User,Profile,Image,Follow
import datetime as dt

class ProfileTest(TestCase):
    """class for testing the class Profile."""
    def setUp(self):
        self.juru = Profile(prof_pic = 'Test Image',bio = 'Test',contact = 'Test')

    def test_instance(self):
        self.assertTrue(isinstance(self.juru,Profile))

    def test_save(self):
        self.juru.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) >0 )

class PostTest(TestCase):
    """Test class to test the class Post."""
    def setUp(self):
        self.juru = Profile(prof_pic = 'Test Image',bio = 'Test',contact = 'Test')
        self.juru.save_profile()

        self.new_post = Post(profile = self.juru, name = 'Test', image = 'Test Image', description = 'Test')

    def tearDown(self):
        Profile.objects.all().delete()
        Comment.objects.all().delete()
        Post.objects.all().delete()

    def test_save(self):
        self.new_post.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) >0 )

class CommentTest(TestCase):
    """A class to test the Review class methods"""
    def setUp(self):
        self.juru = Profile(prof_pic = 'Test Image',bio = 'Test',contact = 'Test')
        self.juru.save_profile()

        self.post = Post(profile = self.juru, name = 'Test', image = 'Test Image', description = 'Test')
        self.post.save()

        self.review = Review(post = self.post, comment = 'test')

    def test_save(self):
        self.review.save_review()
        comments = Post.objects.all()
        self.assertTrue(len(comments) >0 )
