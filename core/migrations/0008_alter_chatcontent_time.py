# Generated by Django 4.1.2 on 2023-01-23 17:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_chatcontent_senton_alter_chatcontent_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatcontent',
            name='time',
            field=models.TimeField(default=datetime.time(22, 42, 59, 13285)),
        ),
    ]