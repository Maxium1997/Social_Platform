from django.urls import path, include

from post.views import PostList, PostCreate, PersonalPostList
from post.views import post_comment

urlpatterns = [
    path('', include([
        path('', PostList.as_view(), name='index'),
    ])),

    path('post/', include([
        path('create/', PostCreate.as_view(), name='post_create'),
        path('detail/<slug:slug>', post_comment, name='post_detail'),
        path('personal/', PersonalPostList.as_view(), name='personal_posts'),
    ])),
]