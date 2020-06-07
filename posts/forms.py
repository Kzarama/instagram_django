from django import forms

from posts.models import Post

# Class form of posts
class PostForm(forms.ModelForm):
    # Metadata class
    class Meta:
        # model
        model = Post
        # fields that be show in the template
        fields = ('user', 'profile', 'title', 'photo')