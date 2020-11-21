from django.db import transaction as _transaction
from rest_framework.views import APIView as _APIView
from rest_framework import permissions as _permissions
import rest_framework.response as _response

from .serializers import ListSerializer as _ListSerializer
import lists.models as _models


class IsOwner(_permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return obj.user == request.user


class ListAPIView(_APIView):
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
        print(data)

        instance = self.model.objects.create(user=user, **data)
        print(instance.user)
        serializer = _ListSerializer(instance=instance)

        return _response.Response(data=serializer.data)
