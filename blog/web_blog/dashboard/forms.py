from django import forms
from oscar.core.loading import get_model


class PostForm(forms.ModelForm):
    class Meta:
        model = get_model('web_blog', 'Post')
        fields = ['title', 'content', 'featured_image', 'post_date', 'authour', 'excerpt']
