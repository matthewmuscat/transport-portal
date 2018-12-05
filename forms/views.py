from django.http import HttpResponse


def discrepancies(request):
    return HttpResponse('<h1>DISCREPANCIES FORM.</h1>')


def checkout(request):
    return HttpResponse('<h1>CHECKOUT FORM.</h1>')
