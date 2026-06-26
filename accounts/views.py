from django.shortcuts import render,redirect
from .forms import UserRegisterationForm
from django.contrib.auth.models import User
from django.contrib import messages

def user_register(request):
    if request.method == 'POST':
        form=UserRegisterationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user=User.objects.create_user(cd['username'],cd['email'],cd['password'])
            user.first_name=cd['first_name']
            user.last_name=cd['last_name']
            user.save()
            messages.success(request,'user register successfully','success')
            return redirect('Home')
            
    else:
        form=UserRegisterationForm()
    return render(request,'register.html',{'form':form})


# Create your views here.
