from django.shortcuts import render
from reg.forms import userform, userinfoform
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