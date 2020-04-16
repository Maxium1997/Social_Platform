from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView

from post.models import Post
from post.forms import PostCreateForm

# Create your views here.


class PostList(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'index.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'


@method_decorator(login_required, name='dispatch')
class PostCreate(CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostCreateForm
    context_object_name = 'post'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        return super(PostCreate, self).form_valid(form)

    def get_success_url(self):
        return redirect('index')
