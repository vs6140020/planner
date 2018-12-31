from django.db import models

class Project(models.Model):
	project_name = models.CharField(max_length=30)
	progress = models.IntegerField(default=0)
	def __str__(self):
		return self.project_name

class Task(models.Model):
	content = models.CharField(max_length=50)
	progress = models.CharField(max_length=20)
	project = models.ForeignKey(Project, on_delete= models.CASCADE)
	def __str__(self):
		return self.content
	class Meta:
		ordering = ('content',)

class Subtask(models.Model):
	content = models.CharField(max_length=50)
	progress = models.CharField(max_length=20)
	task = models.ForeignKey(Task, on_delete= models.CASCADE)
	def __str__(self):
		return "%s %s" %(self.content, self.progress)
	class Meta:
		ordering = ('content',)