from rest_framework import serializers as _serializers


class ListSerializer(_serializers.Serializer):
    name = _serializers.CharField()
    date_created = _serializers.DateTimeField(read_only=True)
    is_completed = _serializers.BooleanField(required=False)
    date_completed = _serializers.DateTimeField(required=False)
