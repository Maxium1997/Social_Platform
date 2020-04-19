from django.urls import path, include

from post.views import PostList, PostCreate, PostUpdate, PersonalPostList
from post.views import post_comment
from post.tag import TagList, TagPostList

urlpatterns = [
    path('', include([
        path('', PostList.as_view(), name='index'),
    ])),

    path('post/', include([
        path('create/', PostCreate.as_view(), name='post_create'),
        path('update/<slug:slug>', PostUpdate.as_view(), name='post_update'),
        path('detail/<slug:slug>', post_comment, name='post_detail'),
        path('personal/', PersonalPostList.as_view(), name='personal_posts'),
    ])),

    path('tag/', include([
        path('', TagList.as_view(), name='tags'),
        path('<slug:slug>', TagPostList.as_view(), name='tag_posts'),
    ])),
]