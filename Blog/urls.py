from django.urls import path
from .views import *
app_name='blog'
urlpatterns = [
    path('',blog_list,name='list'),
    path('detail/<int:pk>',blog_detail,name='detail'),
    path('liked/<int:pk>',like_post,name='like'),
    path('disliked/<int:pk>',dislike_post,name='dislike')
]