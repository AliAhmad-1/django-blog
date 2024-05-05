from django.shortcuts import render
from .forms import RegisterForm,LoginForm,UpdateImageForm,ChangePasswordForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.INFO,'Your account created successfully')

            return HttpResponseRedirect('/')

    else:
        form=RegisterForm()
    return render(request,'register.html',context={'form':form})
def user_login(request):
    
    if request.method=='POST':
        form=LoginForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                next_url=request.GET.get('next','')
                if next_url:
                    return HttpResponseRedirect(next_url)
                else:
                    return HttpResponseRedirect('/')
    else:
        form=LoginForm()

    return render(request,'login.html',{'form':form})

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/account/login')




def edit_profile(request):
    if request.method=='POST':
        form=UpdateImageForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your profile data updated successfully .')
            return HttpResponseRedirect('/')

    else:
        form=UpdateImageForm(instance=request.user)
      
    return render(request,'editprofile2.html',{'form':form})

def password_change(request):
    user_id=request.user.id
    if request.method=='POST':
        form=ChangePasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,request.user)
            messages.add_message(request,messages.INFO,'Your password changed successfully')
            return HttpResponseRedirect(f'/profile/{user_id}')
    else:
        form=ChangePasswordForm(request.user)
    return render(request,'password_change2.html',{'form':form})

