# Generated by Django 2.1.5 on 2019-01-24 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='avatar',
        ),
    ]
