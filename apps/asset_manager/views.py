from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>This page is currently under construction.</h1>')
