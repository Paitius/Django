from hashlib import sha1
from .models import Url
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError


def get_validation_error(url):
    try:
        url.full_clean()
        return None
    except ValidationError as error:
        return '; '.join(error.messages)


def index(request):
    return render(request, 'index.html')


def shorten(request):
    if request.method != 'POST':
        return redirect('index')

    long_url = request.POST['url']
    url_hash = sha1(long_url.encode('utf-8')).hexdigest()
    root = request.get_host()
    short_url = f'{root}/{url_hash}'

    if Url.objects.filter(short=url_hash).exists():
        url = Url.objects.get(short=url_hash)
    else:
        url = Url(short=url_hash, long=long_url)
        validation_errors = get_validation_error(url)
        if validation_errors:
            return render(request, 'message.html', {'message': validation_errors})
        url.save()

    template_tags = {'shorten_url': short_url, 'oryginal_url': url.long}
    return render(request, 'url.html', template_tags)


def redirect_go_to(request, hash):
    if Url.objects.filter(short=hash).exists():
        url = Url.objects.get(short=hash)
        original_url = url.long
        return redirect(original_url)

    message = 'no Url with that hash avainable'
    return render(request, 'message.html', message)
    