from django.db import transaction as _transaction
from django.shortcuts import get_object_or_404 as _get_object_or_404
from rest_framework.views import APIView as _APIView
from rest_framework import permissions as _permissions, status as _status
import rest_framework.response as _response

from .serializers import ListSerializer as _ListSerializer
import lists.models as _models


class IsOwner(_permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class ListAPIView(_APIView):
    """
    Will display all of the lists that have been created.
    """

    permission_classes = [
        _permissions.IsAuthenticated,
        IsOwner,
    ]
    model = _models.List

    def get(self, request):
        user = request.user
        user_lists = self.model.objects.filter(user=user)
        serializer = _ListSerializer(user_lists, many=True)

        return _response.Response(data=serializer.data)

    @_transaction.atomic
    def post(self, request):
        user = request.user
        serializer = _ListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        instance = self.model.objects.create(user=user, **data)
        serializer = _ListSerializer(instance=instance)

        return _response.Response(data=serializer.data)


class ListDetailAPIView(_APIView):

    permission_classes = [
        _permissions.IsAuthenticated,
        IsOwner,
    ]

    model = _models.List

    def get(self, request, list_id):
        user = request.user
        list_obj = _get_object_or_404(self.model, pk=list_id)
        if list_obj.user != user:
            return _response.Response(status=_status.HTTP_404_NOT_FOUND)

        serializer = _ListSerializer(list_obj)

        return _response.Response(data=serializer.data)
