import os
import re
from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from .models import File
from django.db.models import Q


@api_view(['GET'])
def files_api(request):
    files = File.objects.all()
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def filtered_files_api(request):
    filter_str = request.GET.get('filter', '')
    filters = Q()
    filter_map = {
        'name': 'name__icontains',
        'dir': 'path__icontains',
        'ext': 'ext__icontains',
        'crtd': 'created_at__gte',
        'upd': 'modified_at__gte',
        'size': 'size__gte',
    }
    for filter_part in filter_str.split():
        match = re.match(r'^(.+):(.+)$', filter_part)
        if match:
            key = match.group(1)
            value = match.group(2)
            if key in filter_map:
                if key == 'size':
                    size_filter = re.match(r'^(\d+)([KMG]?)$', value)
                    if size_filter:
                        size = float(size_filter.group(1))
                        unit = size_filter.group(2)
                        if unit == 'K':
                            size *= 1024
                        elif unit == 'M':
                            size *= 1024 * 1024
                        elif unit == 'G':
                            size *= 1024 * 1024 * 1024
                        filters &= Q(**{filter_map[key]: size})
                elif key in ['crtd', 'upd']:
                    try:
                        date = datetime.strptime(value, '%Y/%m/%d')
                        filters &= Q(**{filter_map[key]: date})
                    except ValueError:
                        pass
                else:
                    filters &= Q(**{filter_map[key]: value})
    files = File.objects.filter(filters)
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def fill_db_api(request):
    fill_db()
    return Response(status=status.HTTP_200_OK)

def fill_db():
    directory_path = 'D:/Projects/DirManager/DirManager/files_examples'

    files = os.listdir(directory_path)

    for file_name in files:
        file_path = os.path.join(directory_path, file_name)
        file_stat = os.stat(file_path)

        file = File(
            name=file_name,
            path=file_path,
            size=file_stat.st_size,
            created_at=datetime.fromtimestamp(file_stat.st_ctime),
            modified_at=datetime.fromtimestamp(file_stat.st_mtime),
            ext=os.path.splitext(file_name)[1]
        )
        file.save()
