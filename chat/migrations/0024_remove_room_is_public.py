# Generated by Django 3.0.7 on 2020-06-23 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0023_remove_room_user_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='is_public',
        ),
    ]
