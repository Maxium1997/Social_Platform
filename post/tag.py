from post.models import Post, Tag


def processor(post: Post, tag_str: str):
    tags = tag_str.split(' ')
    tagList = [_.name for _ in Tag.objects.all()]

    for tag in tags:
        tag = tag.lower()
        if tag not in tagList:
            Tag.objects.create(name=tag, slug=tag).save()
        post.tags.add(Tag.objects.get(name=tag))

    return post
