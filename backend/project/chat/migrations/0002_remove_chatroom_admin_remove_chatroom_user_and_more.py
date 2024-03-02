# Generated by Django 5.0 on 2024-02-24 13:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='chatroom',
            name='user',
        ),
        migrations.AddField(
            model_name='chatroom',
            name='provider',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='provider_room', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='username',
            field=models.CharField(default='', max_length=255),
        ),
    ]