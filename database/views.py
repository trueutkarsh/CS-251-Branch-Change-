
from django.shortcuts import render, render_to_response,redirect
from django.http import  HttpResponse
from django.shortcuts import render
from database.models import *
from database.forms import studentform
from django.db.models import Q
from django.contrib import  auth
from django.contrib.auth.models import User,UserManager
from authentication.authenticator import ldapAuth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.conf.global_settings import LOGIN_URL
# Create your views here.


def getdata(request):


    errors=[]
    if request.method== 'POST':
        #form=studentform(request.POST)
        stud=student()
        print(request.POST.get("name"))
        stud.name=request.POST.get("name")
        stud.rollno=request.POST.get("rollno")
        pbranch=request.POST.get("pbranch")
        stud.presentbranch=program.objects.all().get(name=pbranch)
        stud.category=request.POST.get("cat")
        '''
        //get all the categories here
        '''
        for x in range(20):
            if request.POST.has_key("pref"+str(x)):
                stud.branchops.add(program.objects.all().get(name=request.POST.get("pref"+str(x))))
            else:
                break
        stud.save()
        '''
        if form.is_valid():
            args={}
            args['form']=form
            args.update(csrf(request))
            return render(request, 'form/branchchangehtml/form.html',args)
        else:
            args={}
            args['form']=form
            args.update(csrf(request))
            return render(request, 'form/input.html',args)
        '''
        return render(request,'form/thanks.html')
    else:
        #if form is empty redict it back
        return render(request, 'form/branchchangehtml/form.html')
