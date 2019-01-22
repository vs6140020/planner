from . models import Project, Task, Subtask

def updateToDatabase(content, taskOrSubtask):
	print('comes to update database')
	if(taskOrSubtask == 'task'):
		try:
			task = Task.objects.get(content = content)
			if(task.progress == 'done'):
				task.progress = 'not-done'
			elif(task.progress =='not-done'):
				task.progress ='done'
			task.save()
		except:
			print('No task found with this task content.')
	else:
		try:
			subtask = Subtask.objects.get(content = content)
			if(subtask.progress == 'done'):
				subtask.progress = 'not-done'
			elif(subtask.progress =='not-done'):
				subtask.progress ='done'
			subtask.save()
		except:
			print('No subtask found with this subtask content.')
	refreshStructure()

def refreshStructure():
	print('comes to refresh structure')
	for project in Project.objects.all():
		for task in project.task_set.all():
			num = 0
			numberOfSubtasks = len(task.subtask_set.all())
			if(numberOfSubtasks != 0):
				for subtask in task.subtask_set.all():
					if(subtask.progress == 'done'):
						num=num+1
					else:
						num=num-1
				if(num == numberOfSubtasks):
					task.progress = 'done'
				elif(num == -(numberOfSubtasks)):
					task.progress = 'not-done'
				else:
					if(task.progress == 'done' or task.progress =='not-done'):
						task.progress = 'partially-done'
			task.save()