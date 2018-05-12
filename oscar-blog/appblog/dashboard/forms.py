from oscar.core.loading import get_model
from oscar.forms import widgets

from django import forms
from django.utils.translation import ugettext_lazy as _


class PostForm(forms.ModelForm):
    post_date = forms.DateField(
        label=_("Post date"), widget=widgets.DatePickerInput)

    class Meta:
        model = get_model('appblog', 'Post')
        fields = ['title', 'content', 'featured_image', 'post_date', 'author', 'excerpt']


class CategoryGroupForm(forms.ModelForm):
    class Meta:
        model = get_model('appblog', 'CategoryGroup')
        fields = ['category', 'post']


class PostSearchForm(forms.Form):
    title = forms.CharField(required=False, label=_("Title"))
    author = forms.CharField(required=False, label=_("Author"))

    class Meta:
        fields = ['title', 'author']

    def clean(self):
        cleaned_data = super(PostSearchForm, self).clean()
        cleaned_data['title'] = cleaned_data['title']
        cleaned_data['author'] = cleaned_data['author']
        return cleaned_data
