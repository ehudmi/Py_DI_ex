# Generated by Django 4.2.6 on 2023-10-20 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0002_alter_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
