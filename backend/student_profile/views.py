from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView
from student_profile.forms import DocumentForm,EmailForm
from student_profile.models import Document
from io import StringIO, BytesIO
from .email import send_mail
from django.template.defaulttags import register
import random
import hashlib
import django
import os

from .sql import insert,fetch

class allStudents(TemplateView):
    def get(self, request, **kwargs):
        data=Document.objects.all()
        new=[]
        print(kwargs)
        for i in list(range(0,len(data)-3,3)):
            new.append(data[i:i+3])
  
        print(len(data)-int(len(data)%3),len(data),new)
        args={"data":data,"set":new,"remaining": data[len(data)-int(len(data)%3):len(data)] }
        print(args)
        return render(request, 'students_profile.html', args)

def model_form_upload(request,code,email):
    print(code,email)
    print(fetch(email))
    if fetch(email):
        if code in fetch(email):
            if request.method == 'POST':
                form = DocumentForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    
            else:
                form = DocumentForm(initial={'email':email+"@iiit-bh.ac.in"})
            return render(request, 'model_form_upload.html', {
                'form': form
            })
        else:
            return HttpResponse('Sorry your code is wrong')
    else:
        return HttpResponse('Sorry your code is wrong')

def Email_checker(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            code='%32x' % random.getrandbits(16*8)
            send_mail(code,email)
            insert(email.split("@")[0],code)
            
    else:
        form = EmailForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })



@register.filter
def get_range(value):
    return range(value)

@register.filter
def get_path(pt):
    print(pt)
    pt=str(pt)
    pt=pt.split("static")
    return pt[-1]

@register.filter
def id_extract(email):
    return email.split("@")[0]
