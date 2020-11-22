from django.shortcuts import render as _render, get_object_or_404 as _get_object_or_404
import django.views.defaults as _defaults


from . import models as _models


def add_item(request, list_id):
    # get the list using the list_id
    list_obj = _get_object_or_404(_models.List, pk=list_id)
    if list_obj.user != request.user:
        return _defaults.page_not_found()

    # ensure that the list belongs to the auth user

    return _render(request, "pages/lists/add_item.html")


def create_list(request):
    return _render(request, "pages/lists/create_list.html")