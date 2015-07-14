from django.shortcuts import render
from .models import Homework
from django.http import HttpResponse

# Create your views here.

def listing(request):
    all_homeworks = Homework.objects.all()
    
        
    return render(request, 'homework/index.html', {"homeworks":all_homeworks})
    #return HttpResponse("<p>" + str(Homework.objects.all()) + "</p>")

def details(request, hw_id):
    
    this_homework = [Homework.objects.get(id=hw_id)]
    return render(request, 'homework/index.html', {"homeworks":this_homework})