"""todo_project URL Configuration """

# importing required packages

from django.contrib import admin
from django.conf.urls import url
from todo.views import home_new_view, \
    change_task_status, TaskList, add_subtask, ChangeStatus, SearchQuery, search_query_view, \
    FilterTask, filter_task_view, soft_delete_task

# url pattern regex with corresponding view

urlpatterns = [
    url(r'^$', home_new_view.as_view(), name='home_view'),
    url(r'^subtask/(?P<task_id>[0-9]+)$', add_subtask, name='add_subtask'),
    url(r'api/filter/category=(?P<query>\w+)$', FilterTask.as_view(), name='filter_task'),
    url(r'^search', search_query_view, name="search_task"),
    url('^filter=(?P<query>\w+)$', filter_task_view, name='filter_task'),
    url(r'^delete/(?P<task_id>[0-9]+)$', soft_delete_task, name='soft_delete'),
    url(r'^admin/', admin.site.urls),
    url(r'change_status/(?P<task_id>[0-9]+)$', change_task_status, name='change_status'),
    url(r'^api/change_status=(?P<task_id>[0-9]+)$', ChangeStatus.as_view(), name='api_change_status'),
    url(r'^api/search/query=(?P<query>\w+)$', SearchQuery.as_view(), name='api_search_query'),
    url(r'^api/task_list', TaskList.as_view(), name='task_list'),
]
