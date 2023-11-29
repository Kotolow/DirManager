from django.db import models


class File(models.Model):

    name = models.CharField(max_length=120)
    path = models.CharField(max_length=500)
    size = models.FloatField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    ext = models.CharField(max_length=10)
