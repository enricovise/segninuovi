from django.views.generic import DetailView
from scuoladsc.models import Edition

class EditionDetailView(DetailView):

    model = Edition

    def get_context_data(self, **kwargs):
        context = super(EditionDetailView, self).get_context_data(**kwargs)
        context['references']= self.get_object().get_references()
        return context

