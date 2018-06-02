from django import forms


class SearchPostForm(forms.Form):
    search = forms.CharField(required=False, label='')

    class Meta:
        fields = ['search']
