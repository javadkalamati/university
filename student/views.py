from django.shortcuts import render
from .models import Person



def home(request):
    students=Person.objects.all()
    return render(request,'home.html',{'student':students})

def detail(request,person_id):
    student = Person.objects.get(id=person_id)
    return render(request,'details.html',{"student":student})
# Create your views here.
