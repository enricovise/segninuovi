from django.conf.urls import patterns, url
from django.views.generic import ListView
from newsletter.models import Issue
from newsletter.views import *

urlpatterns = patterns(
    '',
    url(r'^$', ListView.as_view(model=Issue), name='issue_list'),
    url(r'^(?P<number>\w+)/$', IssueDetailView.as_view(),
        name="issue_detail"),
    url(r'^(?P<number>\w+)/email/$', IssueDetailEmailView.as_view(),
        name="issue_detail_email"),
)
