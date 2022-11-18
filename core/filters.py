import django_filters
from django import forms

from core.models import Link, Tag

class LinkFilter(django_filters.FilterSet):
    tags = django_filters.ModelChoiceFilter(queryset=Tag.objects.all(), label= 'Search by tags', widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Link
        fields = ('tags',)



