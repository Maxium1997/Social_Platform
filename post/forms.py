from django import forms

from post.models import Post, Comment, Tag


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    content = forms.Textarea
    slug = forms.TextInput
    tags = forms.ChoiceField(choices=Tag.objects.all(), widget=forms.Select, required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'slug', 'tags']


class CommentCreateForm(forms.ModelForm):
    # content = forms.Textarea(attrs={'rows': 4, 'cols': 100})
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 4,
                                                                          'cols': 85,
                                                                          'class': 'form_control'}))

    class Meta:
        model = Comment
        widgets = {

        }
        fields = ('content',)
