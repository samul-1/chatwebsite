# Generated by Django 3.0.7 on 2020-06-23 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0016_remove_room_is_public'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='user_1',
        ),
        migrations.RemoveField(
            model_name='room',
            name='user_2',
        ),
    ]