from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='home'),
    path('save_tag', views.save_tag, name='save_tag'),
    path('save_link', views.save_link, name='save_link')
]