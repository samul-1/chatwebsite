# Generated by Django 3.0.7 on 2020-07-15 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0035_attachment_uploaded_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='selected_colorset',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='chat.Colorset'),
        ),
    ]
