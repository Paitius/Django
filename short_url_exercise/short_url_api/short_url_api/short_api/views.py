# from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UrlSerializer
from rest_framework import status
from hashlib import sha1
from .models import Url
from django.core.exceptions import ValidationError


def get_validation_error(url):
    try:
        url.full_clean()
        return None
    except ValidationError as error:
        return '; '.join(error.messages)


@api_view(['GET'])
def index(request):
    data = {'hello': 'Hello'}
    return Response(data)


@api_view(['POST'])
def shorten(request):
    oryginal_url = request.data['url']
    url_hash = sha1(oryginal_url.encode('utf-8')).hexdigest()
    root = request.get_host()

    if Url.objects.filter(short=url_hash).exists():
        url = Url.objects.get(short=url_hash)
    else:
        url = Url(short=url_hash, long=oryginal_url)
        validation_errors = get_validation_error(url)
        if validation_errors:
            data = {'message': validation_errors}
            Response(data, status.HTTP_400_BAD_REQUEST)
        url.save()

    short_url = f'{root}/{url.short}'
    data = {'shorten_url': short_url, 'oryginal_url': url.long}
    return Response(data)


@api_view(['GET'])
def get_original(request, hash):
    if Url.objects.filter(short=hash).exists():
        url = Url.objects.get(short=hash)
        serializer = UrlSerializer(url)
        return Response(serializer.data)

    data = {'message': 'validation_errors'}
    Response(data, status.HTTP_400_BAD_REQUEST)
