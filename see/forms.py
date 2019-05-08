from django import forms
from .models import Profile,Post,Comment

class NewProfForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

    # def __init__(self, *args, **kwargs):
    #     super(NewProfForm, self).__init__(*args, **kwargs)
        # self.fields['prof_pic'].required = False

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['profile','pub_date']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
