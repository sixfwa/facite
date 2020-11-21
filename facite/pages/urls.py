from django.urls import path as _path

from . import views as _views

urlpatterns = [
    _path(
        "",
        _views.index,
        name="index",
    ),
]
