from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from scuoladsc.models import Edition
from scuoladsc.views import EditionDetailView

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Edition), name='edition_list'),
    url(r'^(?P<slug>\w+)/$', EditionDetailView.as_view(),
        name='edition_detail'),
)
