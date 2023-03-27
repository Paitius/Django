from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializer import TaskSerializer
from django.core.exceptions import ObjectDoesNotExist


def safe_get(model, default=None, **kargs):
    try:
        return model.objects.get(**kargs)
    except ObjectDoesNotExist:
        return default


@api_view(['GET'])
def index(request):
    data = {'hello': 'Hello'}
    return Response(data)


@api_view(['GET'])
def list_tasks(request):
    all_tasks = Task.objects.all()
    serializer = TaskSerializer(all_tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_data(request, id):
    task = safe_get(Task, id=id)
    if not task:
        error = {'error': 'not task with such id'}
        return Response(error, status.HTTP_400_BAD_REQUEST)
    serializer = TaskSerializer(task)
    return Response(serializer.data)
