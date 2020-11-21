from django.urls import path as _path

from .api import views as _views

urlpatterns = [
    _path("lists/", _views.ListAPIView.as_view(), name="lists"),
]
