from django.urls import path, include

from post.views import PostList, PostDetail, PostCreate

urlpatterns = [
    path('', include([
        path('', PostList.as_view(), name='index'),
    ])),

    path('post/', include([
        path('create/', PostCreate.as_view(), name='post_create'),
        path('detail/<slug:slug>', PostDetail.as_view(), name='post_detail'),
    ]))
]