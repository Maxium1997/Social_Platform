from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from django.core.exceptions import PermissionDenied
from django.template.defaultfilters import slugify

from registration.models import User
from post.models import Post, Comment
from post.forms import PostCreateForm, PostUpdateForm, CommentCreateForm
from post.tag import processor
from post.collection import collection_add, collection_remove

# Create your views here.


class PostList(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'index.html'
    context_object_name = 'posts'


@login_required
def post_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = CommentCreateForm(request.POST)

        if form.is_valid():
            new_comment = Comment.objects.create(content=form.cleaned_data['content'],
                                                 commenter=request.user)
            new_comment.save()
            post.comment.add(new_comment)

        return redirect('post_detail', slug=post.slug)

    else:
        form = CommentCreateForm()
        context = {'post': post, 'form': form}
        return render(request, 'post/detail.html', context)


# class PostDetail(DetailView):
#     model = Post
#     template_name = 'detail.html'


@method_decorator(login_required, name='dispatch')
class PostCreate(CreateView):
    model = Post
    template_name = 'post/create.html'
    form_class = PostCreateForm
    context_object_name = 'post'

    def form_valid(self, form):
        post = form.save(commit=False)
        post = slugify(post.title)
        post.author = self.request.user
        post.save()
        # post.tag.processor
        processor(post, form.cleaned_data['tags'])
        return redirect('index')

    def get_success_url(self):
        return redirect('index')


# Unfinished
@method_decorator(login_required, name='dispatch')
class PostUpdate(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name_suffix = '_update'

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if request.user != post.author:
            raise PermissionDenied
        return super(PostUpdate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        post = form.save(commit=False)


@method_decorator(login_required, name='dispatch')
class PersonalPostList(ListView):
    model = Post
    template_name = 'post/personal_posts.html'
    context_object_name = 'personal_posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


@method_decorator(login_required, name='dispatch')
class CollectionPostList(ListView):
    model = User
    template_name = 'post/collections.html'
    context_object_name = 'collection_posts'

    def get_queryset(self):
        return self.request.user.collection.posts.all()


# redirect field doesn't work
@login_required(redirect_field_name='post/personal_posts.html')
def post_saved(request, slug):
    post = Post.objects.get(slug=slug)
    collection_add(request.user, post)
    return redirect(request.META.get('HTTP_REFERER'))


# redirect field doesn't work
@login_required(redirect_field_name='post/personal_posts.html')
def post_unsaved(request, slug):
    post = Post.objects.get(slug=slug)
    collection_remove(request.user, post)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(redirect_field_name='post/personal_posts.html')
def post_like(request, slug):
    post = Post.objects.get(slug=slug)
    post.likes.add(request.user)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(redirect_field_name='post/personal_posts.html')
def post_dislike(request, slug):
    post = Post.objects.get(slug=slug)
    post.likes.remove(request.user)
    return redirect(request.META.get('HTTP_REFERER'))
