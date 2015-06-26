from django.conf.urls import patterns, url
from todo import views
urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	
	url(r'^addTodo/', views.newTask,name = 'newTask'),
	url(r'^saveTask/',views.saveTask,name = 'saveTask'),
	url(r'^deleteTask/(?P<taskId>[\w\-]+)/$',views.deleteTask, name = "newTask"),
	url(r'^editTask/(?P<taskId>[\w\-]+)/$',views.editTask, name = 'editTask'),
	url(r'^viewTask/(?P<taskId>[\w\-]+)/$',views.viewTask,name='viewTask'),
	url(r'^saveEditedTask/',views.saveEditedTask,name='saveEditedTask'),



	]