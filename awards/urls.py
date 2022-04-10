from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path('^$',views.index,name="home"),
    re_path('^new/post$',views.new_post,name='new-post'),
    re_path('^profiles$',views.profile,name='profile'),
    re_path('^search$',views.search_post,name='search'),
    re_path('^api/award/$',views.AwardList.as_view())
]