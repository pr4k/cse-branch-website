from django.shortcuts import render
from django.views.generic import TemplateView

class crElections(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'Crform.html', context=None)

class mrAndMissCse(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'Mr and Miss Cse.html', context=None)