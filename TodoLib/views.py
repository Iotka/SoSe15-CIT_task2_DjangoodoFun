from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Task
from django.views.generic.edit import CreateView, UpdateView

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
def bearbeiten(request):
	template = loader.get_template('bearbeiten.htm')   
	return HttpResponse(template.render()) 
def impressum(request):
	template = loader.get_template('impressum.htm')   
	return HttpResponse(template.render()) 

class TaskCreate(CreateView):
	model = Task
	fields = ['title','description','deadline','status']

class TaskUpdate(UpdateView):
	model = Task
	fields = ['title','description','deadline','status']



# Create your views here.


