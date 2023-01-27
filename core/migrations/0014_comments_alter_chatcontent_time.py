# Generated by Django 4.1.2 on 2023-01-25 10:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_chatcontent_time_alter_posttest_userpro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='chatcontent',
            name='time',
            field=models.TimeField(default=datetime.time(16, 14, 19, 194283)),
        ),
    ]
