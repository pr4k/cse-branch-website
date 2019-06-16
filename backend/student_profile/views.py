from django.shortcuts import render
from django.views.generic import TemplateView
from student_profile.forms import DocumentForm
from student_profile.models import Document
class allStudents(TemplateView):
    def get(self, request, **kwargs):
        data=Document.objects.all()
        print(data)
        args={"data":data}
        return render(request, 'students_profile.html', args)

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })