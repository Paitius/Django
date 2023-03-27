from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('task', views.list_tasks, name='task_list'),
    path('task/<id>', views.task_data, name='task_data'),
]
