from django.shortcuts import render, render_to_response, redirect,HttpResponseRedirect
from django.template import RequestContext
from authenticator import ldapAuth
from django.contrib.auth.models import User,UserManager
from django.contrib import  auth
from django.core.urlresolvers import *


# Create your views here.


def authentication(request):
    print("13")
    context = RequestContext(request)
    if request.method == 'POST':
        print("16")
        Username = request.POST["username"]
        Password = request.POST["passwd"]
        #prevpage=request.session.get('prevlogin','/')
        authenticate = ldapAuth(request, Username, Password)
        print(authenticate)
        if authenticate=='VALID':
            print("")
            return redirect('/input')
        else:
            return render_to_response('authentication/index.html', {'logged': 4,'ecomment':"worong username or password"}, context)
    else:       
        return render_to_response('authentication/index.html', {'logged': 4}, context)




def index(request):
    context = RequestContext(request)
    username = request.session.get('username')
    if username is not None:
        userType = request.session.get('userType')
        if userType == 'f':
            return redirect('/input')
        else:
            return redirect('/input')
    #return render_to_response('authentication/index.html', {'logged': 4}, context)
    print("75")
    return redirect('/login')

def logout(request):
    request.session.flush()
    auth.logout(request)
    return redirect("/")