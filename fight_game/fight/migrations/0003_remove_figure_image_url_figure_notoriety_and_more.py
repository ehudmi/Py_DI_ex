# Generated by Django 4.2.5 on 2023-11-05 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fight', '0002_alter_figure_occupation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='figure',
            name='image_url',
        ),
        migrations.AddField(
            model_name='figure',
            name='notoriety',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='figure',
            name='num_images',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='FigureImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('figure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fight.figure')),
            ],
        ),
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notoriety', models.IntegerField(default=0)),
                ('intelligence', models.IntegerField(default=0)),
                ('strength', models.IntegerField(default=0)),
                ('luck', models.IntegerField(default=0)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player', to='fight.figure')),
            ],
        ),
    ]