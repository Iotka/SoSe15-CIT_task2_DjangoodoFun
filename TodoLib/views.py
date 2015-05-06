from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Task
from .forms import TaskChecker
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
	template = loader.get_template('index.htm')   
	todos=Task.objects.all()
	context=RequestContext(request, {
		'todos':todos,})
	return HttpResponse(template.render(context)) 
def add(request):
	template = loader.get_template('add.htm')   
	return HttpResponse(template.render()) 
def howto(request):
	template = loader.get_template('howto.htm')   
	return HttpResponse(template.render()) 
def impressum(request):
	template = loader.get_template('impressum.htm')   
	return HttpResponse(template.render()) 

class TaskCreate(CreateView):
    model = Task
   
    title = "Add new task"
    form_class = TaskChecker
   

class TaskUpdate(UpdateView):
    model = Task
    
    title = "Edit task"
    form_class = TaskChecker

    
class TaskFinish(UpdateView):
	model = Task
	fields = ['finished']
    
class TaskDelete(DeleteView):
    model = Task
    success_url = index



# Create your views here.


