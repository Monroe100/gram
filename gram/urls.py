
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^profile/',views.profile,name = 'profile'),
    url(r'^create/profile/', views.create_profile, name="createProfile"),
    url(r'^create/post/', views.new_post, name="NewPost"),
    url(r'^home/', views.home, name="home"),
    url(r'^other/profile/(\d+)', views.otherprofiles, name='otherProfiles'),
    url(r'^follow/(\d+)', views.follow, name="follow"),
    url(r'^single/image/(\d+)', views.image, name='singleImage'),
    url(r'^unfollow/(\d+)', views.unfollow, name="unfollow"),
    url(r'^comment/(\d+)', views.new_comment, name='Comment'),
    url(r'^search/', views.search_results, name='search_results'),
]