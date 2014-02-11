from django.conf.urls import patterns, url
from django.views.generic import ListView
from sn.models import Person
from sn.views import *

urlpatterns = patterns(
    '',
    url(r'^$', ListView.as_view(
            queryset=Person.objects.all().order_by('last_name',
                                                   'first_name')),
        name='person_list'),
    url(r'^(?P<slug>\w+)/$', PersonDetailView.as_view(), name="person_detail"),
)
