# Generated by Django 4.2.5 on 2023-10-19 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_share', '0002_follow_album_image_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='number_following',
            field=models.IntegerField(default=0),
        ),
    ]
