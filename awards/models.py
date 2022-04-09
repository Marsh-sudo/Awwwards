from django.db import models
from django.contrib.auth.models import User
import datetime as dt
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField(max_length=300,blank=True)
    name = models.CharField(max_length=150,blank=True)
    profile_pic = models.ImageField(upload_to='images/',default='no-image')



class Post(models.Model):
    title=models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    url = models.URLField(max_length=500)
    photo = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post')
    pub_date = models.DateTimeField(auto_now_add=True,blank=True)


class Rating(models.Model):
    ratings = (
        (0,"0"),
        (1,"1"),
        (2,'2'),
        (3,"3"),
        (4,"4"),
        (5,"5"),
        (6,"6"),
        (7,"7"),
        (8,"8"),
        (9,"9"),
        (10, "10"),
    )
    
    design = models.IntegerField(choices=ratings,default='0',blank=True)
    usability = models.IntegerField(choices=ratings,default='0',blank=True)
    content = models.IntegerField(choices=ratings,default='0',blank=True)
    design_average = models.FloatField(default=0,blank=True)
    usability_average = models.FloatField(default=0,blank=True)
    content_average = models.FloatField(default=0,blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)