from django import forms
from .models import Post, CustomUser, Comment, Hashtag

# from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['place', 'content', 'image', 'hashtag_field']

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']

class SigninForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        labels = {'username': '아이디', 'password': '비밀번호'}

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'nickname', 'phone_number', 'nationality', 'profileimage']
        labels = {'username': '아이디', 'password': '비밀번호', 'nickname': '이름', 'phone_number': '전화번호', 'nationality': '국적', 'profileimage': '프로필사진'}
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
