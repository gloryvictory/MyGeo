# Generated by Django 2.1.7 on 2019-03-21 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compname', models.CharField(max_length=64)),
                ('disk', models.CharField(max_length=1)),
                ('folder', models.CharField(max_length=254)),
                ('fullname', models.CharField(max_length=254)),
                ('filename', models.CharField(max_length=254)),
                ('extension', models.CharField(max_length=16)),
                ('filesize', models.BigIntegerField()),
                ('created', models.DateTimeField()),
                ('added', models.DateTimeField()),
            ],
        ),
    ]