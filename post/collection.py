from post.models import Post
from registration.models import User


def collection_add(user: User, post: Post):
    user.collection.posts.add(post)


def collection_remove(user: User, post: Post):
    user.collection.posts.remove(post)
