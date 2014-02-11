from django.views.generic import DetailView
from newsletter.models import Issue
from chances.models import Post

class IssueDetailView(DetailView):
    model = Issue
    slug_field='number'
    slug_url_kwarg='number'

    def get_context_data(self, **kwargs):
        context = super(IssueDetailView, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.published_range(self.object.start,
                                                            self.object.end)
        return context

class IssueDetailEmailView(IssueDetailView):
    template_name='newsletter/issue_detail_email.html'
