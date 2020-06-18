# Generated by Django 3.0.7 on 2020-06-13 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0006_auto_20200613_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Preferences',
            name='of_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='Preferences',
            name='selected_colorset',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chat.Colorset'),
        ),
    ]