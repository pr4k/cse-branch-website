from django.shortcuts import render
from django.views.generic import TemplateView

class allStudents(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'students_profile.html', context=None)
