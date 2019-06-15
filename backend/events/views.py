from django.shortcuts import render
from django.views.generic import TemplateView

class eventspage(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'college_events.html', context=None)
