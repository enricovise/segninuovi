from django.shortcuts import render_to_response, get_object_or_404
from sn.models import Person
from django.views.generic import DetailView

class PersonDetailView(DetailView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        context['neighborhood'] = self.get_object().get_neighborhood(20)
        context['materials'] = self.get_object().materials.all()
        return context
