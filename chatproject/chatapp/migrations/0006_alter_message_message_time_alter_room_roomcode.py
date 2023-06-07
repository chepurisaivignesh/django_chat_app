# Generated by Django 4.1.4 on 2022-12-15 19:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0005_alter_message_message_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 16, 1, 0, 8, 436874)),
        ),
        migrations.AlterField(
            model_name='room',
            name='roomcode',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
