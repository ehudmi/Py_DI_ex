# Generated by Django 4.2.6 on 2023-10-21 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0005_alter_book_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]