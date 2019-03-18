from django.db import models
from django.core.validators import FileExtensionValidator


class UploadFile(models.Model):
    file = models.FileField(upload_to='tmp/', validators=[FileExtensionValidator(allowed_extensions=['csv'])])
