from django.test import TestCase

from .models import User
import datetime as dt

class UserTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.james= User(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,User))
    # Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)

class ImageTestClass(TestCase):
    def setUp(self):
        # Creating a new user and saving it
        self.assumpta= User(first_name = 'Assumpta', last_name ='Uwanyirijuru', email ='jurassu10@gmail.com')
        self.assumpta.save_editor()
        # Creating a new comment and saving it
        self.new_c = Comment(comment = 'comment')
        self.new_c.save()
        # Creating a new like and saving it
        self.new_l = Like(like = 1)
        self.new_l.save()
        # Creating a new img and saving it
        self.new_img= Image(name = 'Test Image',description = 'This is a random test Post',editor = self.assumpta,location = self.new_loc,category = self.new_cat)
        self.new_img.save()

    def tearDown(self):
        User.objects.all().delete()
        Comment.objects.all().delete()
        Like.objects.all().delete()
        Image.objects.all().delete()

    def test_get_image_today(self):
        today_image = Image.todays_image()
        self.assertTrue(len(today_image)>0)

    def test_get_image_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        image_by_date = Image.days_image(date)
        self.assertTrue(len(image_by_date) == 0)

class CommentTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.comment= Comment(comment = 'This is just Beautiful')

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comment))
    # Testing Save Method
    def test_save_method(self):
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) > 0)

class LikeTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.like= Like(like = 1)

    def test_instance(self):
        self.assertTrue(isinstance(self.like,Like))
    # Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        likes = Like.objects.all()
        self.assertTrue(len(likes) > 0)
