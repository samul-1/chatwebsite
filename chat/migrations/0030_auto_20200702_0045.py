# Generated by Django 3.0.7 on 2020-07-01 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0029_message_in_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_banned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]
