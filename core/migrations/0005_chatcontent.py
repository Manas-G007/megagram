# Generated by Django 4.1.2 on 2023-01-23 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_followerscount'),
    ]

    operations = [
        migrations.CreateModel(
            name='chatContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('reciever', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=500)),
                ('time', models.CharField(max_length=20)),
            ],
        ),
    ]