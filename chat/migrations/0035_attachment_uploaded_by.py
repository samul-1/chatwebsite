# Generated by Django 3.0.7 on 2020-07-12 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0034_auto_20200712_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='uploaded_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
