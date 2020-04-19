from django.views.generic import ListView

from post.models import Post, Tag


def processor(post: Post, tag_str: str):
    tag_str = tag_str.replace(" ", "").lower()
    tagList = [_.name for _ in Tag.objects.all()]

    if '@' in tag_str:
        tags = tag_str.split('@')[1:]

        for tag in tags:
            if tag not in tagList:
                newTag = Tag.objects.create(name=tag, slug=tag)
                newTag.save()
                post.tags.add(newTag)
            else:
                post.tags.add(Tag.objects.get(name=tag))
    else:
        if tag_str not in tagList:
            newTag = Tag.objects.create(name=tag_str, slug=tag_str)
            newTag.save()
            post.tags.add(newTag)
        else:
            post.tags.add(Tag.objects.get(name=tag_str))

    return post


class TagList(ListView):
    model = Tag
    queryset = Tag.objects.all()
    template_name = 'tag/tag_list.html'
    context_object_name = 'tags'


class TagPostList(ListView):
    model = Tag
    template_name = 'tag/tag_posts.html'
    context_object_name = 'tag_posts'

    def get_queryset(self, *args, **kwargs):
        return Tag.objects.get(slug=self.kwargs['slug']).post_set.all()

    def get_context_data(self, *args, **kwargs):
        kwargs['tag_name'] = self.kwargs['slug']
        return super().get_context_data(**kwargs)
