# Generated by Django 3.0.7 on 2020-07-10 22:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0031_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
