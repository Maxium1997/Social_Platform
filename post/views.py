from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView, CreateView

from post.models import Post, Comment
from post.forms import PostCreateForm, CommentCreateForm
from post.tag import processor

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
        return render(request, 'post_detail.html', context)


# class PostDetail(DetailView):
#     model = Post
#     template_name = 'post_detail.html'


@method_decorator(login_required, name='dispatch')
class PostCreate(CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostCreateForm
    context_object_name = 'post'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        # post.tag.processor
        processor(post, form.cleaned_data['tags'])
        return redirect('index')

    def get_success_url(self):
        return redirect('index')


@method_decorator(login_required, name='dispatch')
class PersonalPostList(ListView):
    model = Post
    template_name = 'personal_posts.html'
    context_object_name = 'personal_posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
