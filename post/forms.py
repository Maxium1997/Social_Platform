from django import forms

from post.models import Post, Tag


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    content = forms.Textarea
    slug = forms.TextInput
    tags = forms.ChoiceField(choices=Tag.objects.all(), widget=forms.Select, required=False)

    class Meta:
        model = Post
        fields = ('title', 'content', 'slug', 'tags')
