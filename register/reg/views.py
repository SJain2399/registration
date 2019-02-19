from django.shortcuts import render
from reg.forms import userform, userinfoform

from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'reg/index.html')

def signup(request):
    registered =False

    if request.method == 'POST':
        user_form=userform(data=request.POST)
        userinfo_form=userinfoform(data=request.POST)

        if user_form.is_valid() and userinfo_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            userinfo=userinfo_form.save(commit=False)
            userinfo.user=user
            userinfo.save()

            registered=True

        else:
            print(user_form.errors,userinfo_form.errors)
    else:
        user_form=userform()
        userinfo_form=userinfoform()

    return render(request,'reg/signup.html',
                             {'registered':registered,
                             'userform':user_form,
                             'userinfoform':userinfo_form })


def user_login(request):
    if request.method=='POST': 
        username=request.POST.get('username')   
        password=request.POST.get('password')
        user=authenticate(username='username',password='password')
        
        if user:
            if user.is_active():
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')

        else:
            return HttpResponse("Invalid login")

    else:
        return render(request,'reg/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))