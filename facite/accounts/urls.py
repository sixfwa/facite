from django.urls import path as _path

from . import views as _views

urlpatterns = [
    _path(
        "create-account/",
        _views.create_account,
        name="create-account",
    ),
]
