from django.db import models
import datetime
from django.contrib.auth.models import User
class Task(models.Model):
	TASK_STATUS = (
		("Done","Done"),
		("Doing","Doing"),
		("Todo","Todo"),
		)
	taskName = models.CharField(max_length = 100)
	taskDescription = models.TextField(default = "")
	taskDueDate = models.DateField(default = datetime.date.today)
	taskPriority  = models.IntegerField(default = 3)
	taskOwner = models.ForeignKey(User)
	taskStatus = models.CharField(max_length = 5, choices = TASK_STATUS,default="Todo")
	def __unicode__(self):
		return unicode(self.id)


