from django.shortcuts import render,redirect
from .models import Post,Profile,Rating
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import PostForm,UpdateUserProfileForm


# Create your views here.
# @login_required(login_url='/accounts/register/')
def index(request):
    posts = Post.objects.all()
    all_users = User.objects.exclude(id=request.user.id)
    current_user = request.user
    return render(request,'all-awards/home.html',{"posts":posts,"all_users":all_users,"current_user":current_user})

def new_post(request):
    current_user = request.user
    if request.method == "POST":
        post_form = PostForm(request.POST,request.FILES)
        if post_form.is_valid():
            post = post_form.save()
            post = current_user
            post.save()

            return redirect('home')
    else:
        post_form = PostForm()

    return render(request,'all-awards/new_post.html',{"post_form":post_form})


def profile(request):
    profile = Profile.display_profile()
    current_user = request.user
    if request.method == "POST":
        profile_form = UpdateUserProfileForm(request.POST,request.FILES)
        if profile_form.is_valid():
            profile_form.save()
    
    else:
        profile_form = UpdateUserProfileForm()

    return render (request,'all-awards/profile.html',{"profile_form":profile_form,"profiles":profile})


def search_post(request):
    if request.method == 'GET':
        title = request.GET.get("title")
        searched_posts = Post.objects.filter(title__icontains=title).all()

    return render (request,'all-awards/search.html',{"projects":searched_posts})




