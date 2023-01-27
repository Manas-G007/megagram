# Generated by Django 4.1.2 on 2023-01-24 09:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_delete_chatcontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='chatContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('reciever', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=500)),
                ('time', models.TimeField(default=datetime.time(15, 27, 18, 948890))),
            ],
        ),
    ]