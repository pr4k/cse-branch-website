from django.shortcuts import render
from django.views.generic import TemplateView
from student_profile.email import send_query

def contactpage(request):

    if request.method == 'POST':
        print("yep")
        print(request.POST["name"])
        name=request.POST["name"]
        print(request.POST)
        id=request.POST["id"]
        query=request.POST["query"]
        c_id=id[0:3]+str(int(id[3])-1)+id[4:]
        print(c_id)
        send_query(c_id+"@iiit-bh.ac.in",query,name)
        return render(request,'contact.html',context=None)
            
    if request.method == 'GET':
        return render(request, 'contact.html', context=None)
    

