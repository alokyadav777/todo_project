from django.db import models
import datetime, time


# Create your models here.

class Task(models.Model):
    task_id = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    status = models.BooleanField(default=False)
    duedate = models.DateField(default=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d'))
    subtask_of = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class SoftDeletedTask(models.Model):
    soft_task_id = models.IntegerField(default=0)
    soft_task_title = models.CharField(max_length=200)

    def __str__(self):
        return self.soft_task_title

