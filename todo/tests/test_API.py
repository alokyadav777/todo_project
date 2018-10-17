from django.urls import reverse, resolve
from todo.models import Task
import pytest
from mixer.backend.django import  mixer
from django.test import RequestFactory
from todo.views import filter_task_view, SearchQuery
from django.contrib.auth.models import User , AnonymousUser
import requests

class TestUrls:         # test for urls

    def test_task_list_url(self):
        path = reverse('task_list')
        assert resolve(path).view_name == 'task_list'

    def test_change_status_url(self):
        path = reverse('change_status', kwargs={'task_id': 87})
        assert resolve(path).view_name == 'change_status'

    def test_search_task_vie_url(self):
        path = reverse('api_search_query', kwargs={'query': 'sample'})
        assert resolve(path).view_name == 'api_search_query'


class TestModels:       # Test for models

    @pytest.mark.django_db
    def test_task_model(self):
        ta = mixer.blend('todo.Task', task_id = 77)

        assert ta.task_id == 77


class TestViews:            # Test for views

    @pytest.mark.django_db
    def test_filter_task(self):
        path = reverse('filter_task', kwargs= {'query': "week"})
        request = RequestFactory().get(path)
        request.user = AnonymousUser()
        response = filter_task_view(request, query="week")
        assert response.status_code == 200


class TestApiUrl:       # Test Rest API URL

    @pytest.mark.django_db
    def test_api_search_query(self):
        path = reverse('api_search_query', kwargs={'query': "ask"})
        request = RequestFactory().get(path)
        instance = SearchQuery()
        response = instance.get(request, query="ask")
        response
        assert response.status_code == 200




