# Generated by Django 4.2.5 on 2023-09-17 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='category',
            field=models.ManyToManyField(related_name='categories', to='films.category'),
        ),
        migrations.AlterField(
            model_name='film',
            name='created_in_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='countries', to='films.country'),
        ),
        migrations.AlterField(
            model_name='film',
            name='director',
            field=models.ManyToManyField(related_name='directors', to='films.director'),
        ),
    ]
