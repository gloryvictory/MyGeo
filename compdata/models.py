from django.db import models


class CompData(models.Model):
    compname = models.CharField(max_length=64)
    disk = models.CharField(max_length=1)
    folder = models.TextField()
    fullname = models.TextField()
    filename = models.CharField(max_length=254)
    extension = models.CharField(max_length=16)
    filesize = models.BigIntegerField()
    created = models.DateTimeField()
    added = models.DateTimeField()
