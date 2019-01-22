from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . models import Project, Task, Subtask
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .support import updateToDatabase, refreshStructure


# Create your views here.
def default(request):
	if not request.user.is_authenticated:
		return redirect('/login')
	else:
		project_list = Project.objects.all()
		refreshStructure()
		context = {
			'project_list' : project_list,
		}
		return render(request, 'plan/home.html', context)

def template(request, project_name):
	if not request.user.is_authenticated:
		return redirect('/login')
	else:
		task_list = get_object_or_404(Project, project_name = project_name).task_set.all()
		refreshStructure()
		context = {
			'task_list' : task_list,
			'project_name' : project_name,
		}
		return render(request, 'plan/template.html', context)

def loginPage(request):
	context = {}
	return render(request,'plan/login.html', context)

@csrf_exempt
def taskUpdate(request):
	if not request.user.is_authenticated:
		return JsonResponse(null)
	else:
		content = request.POST.get('content', '')
		taskOrSubtask = request.POST.get('taskOrSubtask', '')
		updateToDatabase(content, taskOrSubtask)
		data = {
			'is_updated':True,
		}
		return JsonResponse(data)