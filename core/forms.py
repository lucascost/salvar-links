from django import forms

from core.models import Link, Tag


class LinkForm(forms.ModelForm):
    url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Paste your link here'}))
    tags = forms.ModelMultipleChoiceField(queryset=None)

    class Meta:
        model = Link
        fields = ['url', 'tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tag_list = Tag.objects.all().order_by('name')

        self.fields['tags'].queryset = tag_list
        self.fields['tags'].widget.attrs = {'class':'form-select'}


class TagForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Tag name...'}))

    class Meta:
        model = Tag
        fields = ['name']