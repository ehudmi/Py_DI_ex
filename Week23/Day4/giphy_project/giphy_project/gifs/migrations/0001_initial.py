# Generated by Django 4.2.5 on 2023-09-14 20:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Gif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
                ('url', models.URLField()),
                ('uploader_name', models.CharField()),
                ('created_at', models.DateTimeField(default=datetime.date(2023, 9, 14))),
                ('categories', models.ManyToManyField(to='gifs.category')),
            ],
        ),
    ]
