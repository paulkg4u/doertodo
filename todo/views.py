from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json
from todo.models import Task
from datetime import datetime

@login_required
def index(request):
	
	currentUser = User.objects.get(username = request.user.username)
	contextDi = {}
	
			
			
			
			

	
		
	todoList = Task.objects.filter(taskOwner = currentUser)
	for each in todoList:
		each.taskDescription = each.taskDescription[:15]
	
				
	contextDi['todos'] = todoList
	print "going to return"
	return render(request,'app/index.html',contextDi)





@login_required
def newTask(request):
	return render (request,'app/newTask.html')

@login_required
def  editTask(request,taskId):
	taskObject = Task.objects.get(id = taskId)
	contextDi = {}
	contextDi['task']=taskObject
	print taskObject.taskDueDate

	return render(request,'app/edit-task.html',contextDi)

@login_required
def viewTask(request,taskId):
	contextDi={}
	taskObject=Task.objects.get(id = taskId)
	print taskObject.taskName
	contextDi['task']=taskObject
	return render(request,'app/view-task.html',contextDi)

@login_required
def deleteTask(request,taskId):
	taskObject = Task.objects.get(id = taskId)
	taskObject.delete()
	return HttpResponseRedirect('/todo/')

@login_required
def saveTask(request):
	if request.POST:
		taskData = request.POST

		
		taskName = taskData['taskName']
		taskDescription = taskData['taskDesc']
		taskPriority = taskData['priority']
		taskDate = taskData['dueDate']
		taskOwner = User.objects.get(username = request.user.username)
		taskStatus = "Todo"
		newTaskObject = Task(taskName = taskName,taskDescription=taskDescription,taskDueDate = taskDate,taskPriority=taskPriority,taskOwner=taskOwner,taskStatus=taskStatus)
		newTaskObject.save()
	return HttpResponseRedirect('/todo/')

@login_required
def saveEditedTask(request):
	if request.POST:
		taskData = request.POST
		taskObject = Task.objects.get(id = taskData['taskId'])
		taskObject.taskName =taskData['taskName']
		taskObject.taskDescription = taskData['taskDesc']
		taskObject.taskDueDate=taskData['dueDate']
		taskObject.taskStatus=taskData['taskStatus']
		taskObject.taskPriority = taskData['priority']
		taskObject.save()

	return HttpResponseRedirect('/todo/')
