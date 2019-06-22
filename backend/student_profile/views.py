from django.shortcuts import render,HttpResponse,redirect
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
        print(list(range(0,3-2,3)))
        if len(data)%3==0:
            for i in list(range(0,len(data)-2,3)):
                new.append(data[i:i+3])
        else:
            for i in list(range(0,len(data)-3,3)):
                new.append(data[i:i+3])

  
        args={"data":data,"set":new,"remaining": data[len(data)-int(len(data)%3):len(data)] }
        print(args)
        return render(request, 'students_profile.html', args)

def model_form_upload(request,code,email):
    print(code,email)
    print(fetch(email))
    if fetch(email):
        #if code in fetch(email):
        if code=="3":
            if request.method == 'POST':
                form = DocumentForm(request.POST, request.FILES)
                if form.is_valid():

                    form.save()
                    return redirect('/students')
                    
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
            if email.split("@")[-1]=="iiit-bh.ac.in" and email.split("@")[0][:4].upper()=="B118":
                code='%32x' % random.getrandbits(16*8)
                send_mail(code,email)
                insert(email.split("@")[0],code)
                return redirect('/students')
            else:
                form = EmailForm()
                return render(request, 'model_form_upload.html', {
                    'form': form,"err":1
                })

            
    else:
        form = EmailForm()
    return render(request, 'model_form_upload.html', {
        'form': form,"err":0
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

