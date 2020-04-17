from django.db import models

from registration.models import User
from post.definition import Privacy

# Create your models here.


class Reply(models.Model):
    content = models.TextField()
    responder = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pub_date']


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    photo = models.ImageField(upload_to='images', null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    privacy = models.BooleanField(default=Privacy.Public.value[0])
    slug = models.SlugField(max_length=200, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    comment = models.ManyToManyField(Comment)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
