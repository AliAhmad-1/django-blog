from django import forms
from app.models import CustomUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm
class RegisterForm(UserCreationForm):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Username' }))
    email=forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    password1=forms.CharField(max_length=100,widget=forms.PasswordInput(render_value=True,attrs={'placeholder':'Password'}))
    password2=forms.CharField(max_length=100,widget=forms.PasswordInput(render_value=True,attrs={'placeholder':'confirm password(agin)'}))
    class Meta:
        model=CustomUser
        fields=['username','email','password1','password2']

class LoginForm(AuthenticationForm):

    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Username' }))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(render_value=True,attrs={'placeholder':'Password'}))


    class Meta:
        model=CustomUser
        fields=['username','password']

class UpdateImageForm(UserChangeForm):
    password=None
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    bio=forms.CharField(widget=forms.Textarea(attrs={'rows':3,'placeholder':'Bio'}))
    photo=forms.ImageField(widget=forms.FileInput(attrs={'class':'profile_photo_input'}))
    class Meta:
        model=CustomUser
        fields=['photo','username','email','bio']

class ChangePasswordForm(PasswordChangeForm):
    old_password=None
    new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"New Password"}))
    new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Confirm Password"}))
    class Meta:
        model=CustomUser
        fields=['new_password1','new_password2']
        


        