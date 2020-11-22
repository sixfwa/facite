from django.urls import path as _path

from . import views as _views

urlpatterns = [
    _path("lists/", _views.ListAPIView.as_view(), name="lists"),
    _path(
        "lists/<int:list_id>/", _views.ListDetailAPIView.as_view(), name="list-detail"
    ),
]
