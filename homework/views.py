from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render
from .models import Homework
from accounts.models import UserProfile
from django.http import HttpResponse
from .forms import HomeworkForms
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

def details(request, id):
    
    this_homework = [Homework.objects.get(id=id)]
    return render(request, 'homework/index.html', {"object_list":this_homework})
    
class HomeworkCreate(CreateView):
    
    model = Homework
    form_class = HomeworkForms
    success_url = reverse_lazy('homework_list')
    
    def post(self, request, *args, **kwargs):
        
        form_args = {
            'data': self.request.POST,
        }
        
        form = self.form_class(**form_args)
        
        if form.is_valid():
            
        
            curruser = UserProfile.objects.get(user=self.request.user)
            obj = form.save(commit=False)
            obj.user = curruser #Save the note note under that user
            obj.save() #save the new object
        
            return render(request, 'homework/index.html', {"object_list":Homework.objects.filter(user=curruser)})
            
        else:
            
            
            return render(request, 'homework/homework_form.html', {"form":form})
    
class HomeworkUpdate(UpdateView, object):
    model = Homework
    form_class = HomeworkForms
    #success_url = reverse_lazy('homework_list')
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeworkUpdate, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(HomeworkUpdate, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context
        
class HomeworkList(ListView, object):
    model = Homework
    queryset = Homework.objects.all()
    template_name = 'homework/index.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeworkList, self).dispatch(*args, **kwargs)
        
    def get_queryset(self):
        curruser = UserProfile.objects.get(user=self.request.user)
        print curruser
        subject = self.kwargs['subject']
        
        if not subject:
            self.queryset = Homework.objects.filter(user=curruser).order_by('-given_date')

            
        else:
            #filter based on current logged in user
            self.queryset = Homework.objects.all().filter(user=curruser).filter(subject__name__iexact=subject)

        return self.queryset
        
    def get_context_data(self, **kwargs):
        
        context = super(HomeworkList, self).get_context_data(**kwargs)
        context['total'] = self.queryset.count()
        #provided so that the avatar can be displayed in base.html
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        context['username'] = self.request.user.username
        return context
        
    
class HomeworkDelete(DeleteView, object):
    model = Homework
    success_url = '/index/'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeworkDelete, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(HomeworkDelete, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context
        
def home(request):

    return render(request, "homework/home.html")

    