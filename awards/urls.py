from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path('^$',views.index,name="home"),
    re_path('^new/post$',views.new_post,name='new-post'),
]