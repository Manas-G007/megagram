from django.urls import path 
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('settings',views.settings,name='settings'),
    path('upload',views.upload,name='upload'),
    path('like-post',views.like_post,name='like-post'),
    path('comment',views.comment,name='comment'),
    path('saveChat',views.saveChat,name='saveChat'),
    path('follow',views.follow,name='follow'),
    path('search',views.search,name='search'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('profile/<str:pk>',views.profile,name='profile'),
    path('chat/<str:sk>',views.chat,name='chat'),
    path('explore',views.explore,name='explore'),
    path('share/<str:id>',views.share,name='share'),
]