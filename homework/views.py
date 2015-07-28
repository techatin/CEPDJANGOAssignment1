from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render
from .models import Homework
from django.http import HttpResponse
from .forms import HomeworkForms
from django.shortcuts import redirect

# Create your views here.

def details(request, hw_id):
    
    this_homework = [Homework.objects.get(id=hw_id)]
    return render(request, 'homework/index.html', {"homeworks":this_homework})
    
class HomeworkCreate(CreateView):
    
    model = Homework
    form_class = HomeworkForms
    success_url = reverse_lazy('homework_list')
    
class HomeworkUpdate(UpdateView):
    model = Homework
    form_class = HomeworkForms
    
class HomeworkList(ListView):
    model = Homework
    template_name = 'homework/index.html'
    
class HomeworkDelete(DeleteView):
    model = Homework
    success_url = reverse_lazy('homework_list')
    