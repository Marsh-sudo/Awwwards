from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Post,Profile,Rating
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import PostForm,UpdateUserProfileForm,RatingForm
from .serializer import AwardSerializer
from .models import Awards
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
@login_required(login_url='/accounts/register/')
def index(request):
    posts = Post.objects.all()
    all_users = User.objects.exclude(id=request.user.id)
    current_user = request.user
    items = Post.display()


    return render(request,'all-awards/home.html',{"posts":posts,"all_users":all_users,"current_user":current_user,"items":items})

def new_post(request):
    current_user = request.user
    if request.method == "POST":
        post_form = PostForm(request.POST,request.FILES)
        post_form.instance.user = request.user
        print(post_form)
        if post_form.is_valid():
            # post = Post()
            # post.title = post_form.cleaned_data['title']
            # post.description = post_form.cleaned_data['description']
            # post.link = post_form.cleaned_data['link']
            # post.image = post_form.cleaned_data['image']
            # post.user = post_form.cleaned_data['user']
            # post.save()
            post_form.save()

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

    return render (request,'all-awards/profile.html',{"profiles_form":profile_form,"profiles":profile})



def search_post(request):
    if request.method == 'GET':
        title = request.GET.get("title")
        searched_posts = Post.objects.filter(title=title).all()

    return render (request,'all-awards/search.html',{"projects":searched_posts})


class AwardList(APIView):
    def get(self,request,format=None):
        all_award = Awards.objects.all()
        serializers = AwardSerializer(all_award,many=True)
        return Response(serializers.data)

