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

    return render (request,'all-awards/profile.html',{"profiles_form":profile_form,"profiles":profile})


# def ratings(request):
#     post = Post.objects.all()
#     ratings = Rating.objects.filter()
#     if request.method == 'POST':
#         form = RatingForm(request.Post)
#         if form.is_valid():
#             rate_result = form.save()
#             rate_result.save()
#             post_ratings = Rating.objects.filter(post=post)

#             design_rate = [d.design for d in post_ratings]
#             design_av = sum(design_rate) / len(design_rate)

#             usability_rate = [us.usability for us in post_ratings]
#             usability_av  = sum(usability_rate) / len(usability_rate)

#             content_rate = [cont.content for cont in post_ratings]
#             content_av = sum(content_rate) / len(content_rate)

#             total = (design_av + usability_av + content_av) / 3
#             rate_result.design_average = round(design_av, 2)
#             rate_result.usability_average = round(usability_av, 2)
#             rate_result.content_average = round(content_av, 2)
#             rate_result.total = round(total, 2)
#             rate_result.save()
#             return HttpResponseRedirect(request.path_info)
#         else:
#             form = RatingForm()
#         return render(request,'all-awards/rating.html',{"post":post,"ratings":ratings,"rate_form":form})    


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

