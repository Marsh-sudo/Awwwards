from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post,Profile,Rating



class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    
    # specify model it will interact with
    class Meta:
        model = User  
        fields= ['username','email', 'password1','password2']
        
        help_texts = { 'username': None, 'password2': None, }


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('photo','title','url','description')
