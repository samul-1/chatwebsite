# Generated by Django 3.0.7 on 2020-06-23 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0024_remove_room_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]