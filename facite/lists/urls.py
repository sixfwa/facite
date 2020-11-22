from django.urls import path as _path

from . import views as _views

urlpatterns = [
    _path("create-list/", _views.create_list, name="create-list"),
    _path("<int:list_id>/add-item/", _views.add_item, name="add-item"),
]
