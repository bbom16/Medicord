# Generated by Django 2.1.4 on 2019-01-14 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_diary_published_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='meal_contents',
            field=models.CharField(max_length=200),
        ),
    ]
