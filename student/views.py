from django.shortcuts import render,redirect
from .models import Person
from django.contrib import messages
from .forms import StudentCreateForm,StudentUpdateForm


def home(request):
    students=Person.objects.all()
    return render(request,'home.html',{'student':students})

def detail(request,person_id):
    student = Person.objects.get(id=person_id)
    return render(request,'details.html',{"student":student})
def delete(request,person_id):
    Person.objects.get(id=person_id).delete()
    messages.success(request,'student deleted successfully','success')
    return redirect('Home')

def create(request):
    if request.method == 'POST':
        form=StudentCreateForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            Person.objects.create(name=cd['name'],family=cd['family'],mellinumber=cd['mellinumber'],address=cd['address'],birthday=cd['birthday'])
            messages.success(request,"user created successfully",'success')
            return redirect('Home')

    else:
        form=StudentCreateForm()
    return render(request,'create.html',{'form':form})


def update(request,person_id):
    student=Person.objects.get(id=person_id)
    if request.method == 'POST':
        form=StudentUpdateForm(request.POST,instance=student)
        if form.is_valid():
            form.save()#cleaned_data not required
            messages.success(request,"form update successfully","success")
            return redirect('details',person_id)
    else:
        form=StudentUpdateForm(instance=student)# form show last information
    return render(request,'update.html',{'form':form})
# Create your views here.
