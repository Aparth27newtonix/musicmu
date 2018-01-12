
from django.conf.urls import  include ,url
from . import views

app_name = 'music'
#urls for our main app

urlpatterns = [
url(r'^$',views.home_detail,name='home_detail'),
url(r'^SignUp/$',views.SignUp,name='SignUp'),
url(r'^logout/$',views.logout_user,name='logout_user'),
url(r'^login/$',views.login_user,name='login_user'),
 url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
 url(r'^after_login_home/$',views.after_login_home,name='after_login_home'),
  url(r'^(?P<song_id>[0-9]+)/$', views.add, name='add'),
]