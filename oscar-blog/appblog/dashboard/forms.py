from oscar.core.loading import get_model

from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = get_model('appblog', 'Post')
        fields = ['title', 'content', 'featured_image', 'post_date', 'authour', 'excerpt']
