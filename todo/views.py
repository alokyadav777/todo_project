from django.shortcuts import render, HttpResponse, redirect
from todo.forms import Task_Form
from todo.models import Task, SoftDeletedTask
from django.views.generic import TemplateView
from django.core import serializers
import json, requests
from rest_framework.views import APIView
from todo.serializers import TaskSerializers
from rest_framework.response import Response
from random import randint
from datetime import datetime, timedelta
import schedule, time

global_dict = []  # Global variable for dictionary


def get_effective_query(old_task_list):             # function for getting effective query
    new_task_list = []

    for i in old_task_list:
        flag = SoftDeletedTask.objects.filter(soft_task_id=i.task_id).exists()

        if not flag:
            new_task_list.append(i)

    return new_task_list


class home_new_view(TemplateView):      # Home view function

    def get(self, request):
        bin_task = SoftDeletedTask.objects.all()
        context = {'task_list': get_effective_query(Task.objects.all().order_by('duedate')),
                   'forms': Task_Form, 'bintask': SoftDeletedTask.objects.all(), 'bintask': bin_task}
        delete_from_hard_drive()
        return render(request, 'index.html', context)

    def post(self, request):        # post method for accepting forms
        form = Task_Form(request.POST)
        if form.is_valid():
            task_instance = Task(title=form.cleaned_data['Title'], description=form.cleaned_data['Description'],
                                 duedate=form.cleaned_data['Due_date'])
            task_instance.save()
        return redirect('home_view')


def add_subtask(request, task_id):      # Add Subtask into Database using request POST form

    id = Task.objects.all().order_by("-id")[0].task_id + 1
    form = Task_Form(request.POST)
    if form.is_valid():
        task_instance = Task(task_id=id, title=form.cleaned_data['Title'], description=form.cleaned_data['Description'],
                             duedate=form.cleaned_data['Due_date'], subtask_of=task_id)
        task_instance.save()
    return redirect('home_view')


def soft_delete_task(request, task_id):         # soft_delete view for delteling to bin
    total_row = SoftDeletedTask.objects.all().count()
    val = Task.objects.get(task_id=task_id)

    print(val.title)
    soft_instance = SoftDeletedTask.objects.create(soft_task_id=task_id, soft_task_title=val.title)
    soft_instance.save()

    return redirect('home_view')


def get_filtered_task(query):           # view for filtering data based on search_query
    if query == 'today':
        queryset = Task.objects.filter(duedate=datetime.now().strftime("%Y-%m-%d"))

        return queryset

    elif query == 'week':
        day = datetime.now().strftime("%Y-%m-%d")
        today = datetime.strptime(day, '%Y-%m-%d')
        start_date = today - timedelta(days=today.weekday())
        end_date = start_date + timedelta(days=6)
        queryset = Task.objects.filter(duedate__range=[start_date, end_date])
        return queryset

    elif query == 'overdue':        # overdue conndition

        queryset = Task.objects.filter(duedate__lt=datetime.now().strftime("%Y-%m-%d"), status=False)
        return queryset


def filter_task_view(request, query):     #  filter task view
    bin_task = SoftDeletedTask.objects.all()
    val = get_filtered_task(query)
    context = {'task_list':get_effective_query(val) , 'forms': Task_Form, 'bintask': bin_task}
    return render(request, 'index.html', context)


class FilterTask(APIView):      # Filter seriliazable api
    def get(self, request, query):
        return Response(TaskSerializers(get_filtered_task(query), many=True).data)


def change_task_status(request, task_id):  # Change Task status view
    Task.objects.filter(task_id=task_id).update(status=True)
    return redirect('home_view')


class ChangeStatus(APIView):        # class for change status
    def get(self, request, task_id):
        Task.objects.filter(task_id=task_id).update(status=True)
        queryset = Task.objects.filter(task_id=task_id)
        return Response(TaskSerializers(queryset, many=True).data)


def search_query_view(request):                     # search query view for task list
    query = str(request.POST.get("search_task"))
    queryset = Task.objects.filter(title__contains=query)
    context = {'task_list': get_effective_query(queryset), 'forms': Task_Form}
    return render(request, 'index.html', context)


class SearchQuery(APIView):    # search query serializable for api
    def get(self, request, query):
        queryset = Task.objects.filter(title__contains=query)
        ser = TaskSerializers(queryset, many=True)
        return Response(ser.data)


class TaskList(APIView):  # TaskList view function
    def get(self, request):
        co_obj = Task.objects.all()
        ser = TaskSerializers(co_obj, many=True)
        return Response(ser.data)

    def post(self):
        pass




def delete_from_hard_drive():           # Method for removing data from system database
    target_date = str(datetime.now() + timedelta(-30))
    target_date = target_date[:10]

    queryset = Task.objects.all()

    for task in queryset:
        if str(task.duedate) < target_date:
            Task.objects.filter(duedate=task.duedate).delete()
