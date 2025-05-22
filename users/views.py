from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



# Create your views here.


def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,email = cd['email'],password = cd['password'])
            
            if user:
                login(request,user)
                return redirect('shop:index')
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Username or Password incorrect'   
                )
                pass
            # messages
    return render(request,'users/login.html',{'form':form})



def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('shop:index')