from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth.models import User


@api_view(['GET'])
def index(request):
    data = {'Hello': 'hello'}
    return Response(data)
