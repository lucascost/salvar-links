from django.shortcuts import render, redirect

from core.filters import LinkFilter
from core.forms import LinkForm, TagForm


def index(request):
    filter = LinkFilter(request.GET)

    context = {
        'filter': filter,
        'form': LinkForm(),
        'tag_form': TagForm()
    }
    return render(request, 'index.html', context)


def save_tag(request):
    tag_form = TagForm(request.POST)
    if tag_form.is_valid():
        tag_form.save()
    return redirect('/')

def save_link(request):
    link_form = LinkForm(request.POST)
    if link_form.is_valid():
        link_form.save()

    return redirect('/')
