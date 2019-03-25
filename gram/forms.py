from django import forms
from .models import Profile,Image
# class RegistrationForm(forms.ModelForm):
    # email = forms.EmailField(max_length=30,label='Your Email Address',required=True)
    # username = forms.CharField(max_length=30,label='Enter your username',required=True)
    # password = forms.CharField(max_length=30,label='Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    # password_confirm = forms.CharField(max_length=30,label='Confirm Passwords',validators = [Required()])

    # class Meta:
    #     model = Profile
        # fields = ('email','username','password','password_confirm')
    # def validate_email(self,data_field):
    #     if User.objects.filter(email =data_field.data).first():
    #         raise ValidationError('There is an account with that email')
    #
    # def validate_username(self,data_field):
    #     if User.objects.filter(username = data_field.data).first():
    #         raise ValidationError('That username is taken')

# class LoginForm(forms.ModelForm):
#     email = forms.EmailField(label='Your Email Address',validators=[Required(),Email()])
#     password = forms.PasswordField(label='Password',validators =[Required()])
#     remember = forms.BooleanField(label='Remember me')
#     class Meta:
#         model = User
#         fields = ('email','password','remember')

class NewProfForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'pub_date']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }

# class NewFollowForm(forms.ModelForm):
#     class Meta:
#         model = Follow
