# Generated by Django 4.1.2 on 2023-01-24 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_chatcontent_time_alter_profile_bio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='chatContent',
        ),
    ]
