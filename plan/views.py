from django.shortcuts import render
from django.http import HttpResponse
from . models import Project, Task, Subtask
from django.shortcuts import render

# Create your views here.
def default(request):
	project_list = Project.objects.all()
	context = {
		'project_list' : project_list,
	}
	return render(request, 'plan/home.html', context)

def template(request, project_name):
	task_list = Project.objects.get(project_name = project_name).task_set.all()
	context = {
		'task_list' : task_list,
	}
	return render(request, 'plan/template.html', context)