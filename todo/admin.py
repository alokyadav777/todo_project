from django.contrib import admin
from todo.models import Task, SoftDeletedTask

# Register your models here.

admin.site.register(Task)
admin.site.register(SoftDeletedTask)