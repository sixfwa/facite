from django.shortcuts import render as _render


def index(request):

    return _render(request, "pages/home/index.html")