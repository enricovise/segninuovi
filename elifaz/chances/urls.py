from django.conf.urls import patterns, url
from django.views.generic import ListView
from chances.models import Post

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(queryset=Post.objects.select_subclasses()),
        name='post_list'),
)
