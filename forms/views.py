from django.shortcuts import render


def report(request):
    return render(request, "forms/report.html")


def checkout(request):
    return render(request, "forms/checkout.html")
