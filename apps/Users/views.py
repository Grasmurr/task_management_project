from django.shortcuts import render
from django.http import HttpResponseNotAllowed


def registration_view(request):
    if request:
        return render(request, 'main/reg_page.html')
    else:
        return HttpResponseNotAllowed


def login_view(request):
    if request:
        return render(request, 'main/login_page.html')
    else:
        return HttpResponseNotAllowed