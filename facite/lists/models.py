from django.db import models as _models
from django.contrib.auth.models import User as _User


class List(_models.Model):
    class Meta:
        verbose_name = "List"
        verbose_name_plural = "Lists"

    name = _models.CharField(verbose_name="name", max_length=255)
    user = _models.ForeignKey(_User, verbose_name="user", on_delete=_models.CASCADE)
    date_created = _models.DateTimeField(verbose_name="date created", auto_now_add=True)
    is_completed = _models.BooleanField(verbose_name="completed", default=False)
    date_completed = _models.DateTimeField(
        verbose_name="date completed", default=None, null=True
    )


class ListItem(_models.Model):
    class Meta:
        verbose_name = "List Item"
        verbose_name_plural = "List Items"

    item_name = _models.CharField(verbose_name="item name", max_length=255)
    todo_list = _models.ForeignKey(List, verbose_name="list", on_delete=_models.CASCADE)
    date_created = _models.DateTimeField(verbose_name="date created", auto_now_add=True)
    is_completed = _models.BooleanField(verbose_name="completed", default=False)
    date_completed = _models.DateTimeField(verbose_name="date completed", default=None)
