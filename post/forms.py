from django import forms

from post.models import Post, Comment, Tag


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(required=True,
                            max_length=200,
                            widget=forms.TextInput(attrs={'id': 'title',
                                                          'class': 'form-control',
                                                          'onkeyup': 'slugInput();'}))
    content = forms.CharField(required=True,
                              widget=forms.Textarea(attrs={'rows': 10,
                                                           'cols': 50,
                                                           'class': 'form-control'}))
    slug = forms.CharField(required=True,
                           max_length=200,
                           widget=forms.TextInput(attrs={'id': 'slug',
                                                         'class': 'form-control'}))
    tags = forms.CharField(required=False,
                           max_length=200,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'e.g.(health technology art)'}),
                           help_text='Add tags to describe what your post is about.')

    class Meta:
        model = Post
        fields = ['title', 'content', 'slug', 'tags']


class CommentCreateForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 4,
                                                                          'cols': 85,
                                                                          'class': 'form-control'}))

    class Meta:
        model = Comment
        widgets = {

        }
        fields = ('content',)
