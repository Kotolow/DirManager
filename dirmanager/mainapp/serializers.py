from .models import File
from rest_framework import serializers


class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ['name', 'path', 'size', 'created_at', 'modified_at', 'ext']
