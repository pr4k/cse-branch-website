from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from student_profile.email import send_mail,send_application
import random
from .sql import *

class crElections(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'Crform.html', context=None)
    def post(self,request,**kwargs):
        print("yeah")
        print(request.POST)
        try:
            for i in fetch(request.POST["email"].split("@")[0]):
                if i[2]=="CR":
                    return HttpResponse("Sorry you already submitted")
        except Exception as e:
            print(e)
        #print(list(zip(list(request.POST),list(request.POST.values()))))
        fl=open("application/static/database/Crform_{}.txt".format(request.POST["email"].split("@")[0]),"w")
        response=[i+"\n" for i in list(request.POST.values())]
        questions=[i+"\n" for i in list(request.POST)]
        print(questions,response)
        fl.writelines(response[1:])
        fl.close()
        fl=open("application/static/database/Crform_questions.txt","w")
        fl.writelines(questions[1:])
        fl.close()
        code='%32x' % random.getrandbits(16*8)
        
        insert(request.POST["email"].split("@")[0],code,"/static/database/Crform_{}.txt".format(request.POST["email"].split("@")[0]),"CR")
        
        send_mail("forms/verify/"+code,request.POST["email"],"Cr Form")
        return HttpResponse("Check your email")

class mrAndMissCse(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'Mr and Miss Cse.html', context=None)
    def post(self,request,**kwargs):
        print("yeah")
        try:
            for i in fetch(request.POST["email"].split("@")[0]):
                if i[2]=="CSE":
                    return HttpResponse("Sorry you already submitted")
        except Exception as e:
            print(e)#print(list(zip(list(request.POST),list(request.POST.values()))))
        fl=open("application/static/database/Cseform_{}.txt".format(request.POST["email"].split("@")[0]),"w")
        response=[i+"\n" for i in list(request.POST.values())]
        questions=[i+"\n" for i in list(request.POST)]
        print(questions,response)
        fl.writelines(response[1:])
        fl.close()
        fl=open("application/static/database/Cseform_questions.txt","w")
        fl.writelines(questions[1:])
        fl.close()
        code='%32x' % random.getrandbits(16*8)
        
        insert(request.POST["email"].split("@")[0],code,"/static/database/Cseform_{}.txt".format(request.POST["email"].split("@")[0]),"CSE")
        
        send_mail("forms/verify/"+code,request.POST["email"],"Mr and Miss Form")
        return HttpResponse("Check your email")


class verified(TemplateView):
    def get(self,request,code,email):
        print(fetch(email))
        for i in fetch(email):
            if code in i[0] and i[2]=="CR":
                fl=open("application"+i[1],"r")
                answers=fl.readlines()
                print(answers)
                fl=open("application/static/database/Crform_questions.txt","r")
                questions=fl.readlines()
                questions=[i[:-1] for i in questions]
                answers=[i[:-1] for i in answers]
                send_application("CR FORM",questions,answers)
                return render(request,"thanks.html",context=None)

            if code in i[0] and i[2]=="CSE":
                fl=open("application"+i[1],"r")
                answers=fl.readlines()
                print(answers)
                fl=open("application/static/database/Cseform_questions.txt","r")
                questions=fl.readlines()
                questions=[i[:-1] for i in questions]
                answers=[i[:-1] for i in answers]
                send_application("CSE FORM",questions,answers)
                return render(request,"thanks.html",context=None)