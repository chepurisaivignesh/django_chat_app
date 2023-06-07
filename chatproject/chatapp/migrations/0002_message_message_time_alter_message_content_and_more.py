# Generated by Django 4.1.4 on 2022-12-15 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='message',
            name='messenger',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='message',
            name='roomcode',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
