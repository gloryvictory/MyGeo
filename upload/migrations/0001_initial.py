# Generated by Django 2.1.7 on 2019-03-21 09:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='tmp/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['csv'])])),
            ],
        ),
    ]