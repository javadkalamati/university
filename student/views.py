from django.shortcuts import render
from .models import Person



def home(request):
    students=Person.objects.all()
    return render(request,'home.html',{'student':students})

# Create your views here.
