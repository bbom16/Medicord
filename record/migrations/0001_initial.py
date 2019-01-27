# Generated by Django 2.1.5 on 2019-01-23 09:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_date', models.DateField(default=django.utils.timezone.now)),
                ('meal_time', models.TimeField()),
                ('meal_type', models.CharField(max_length=3)),
                ('meal_contents', models.CharField(max_length=200)),
                ('medicine_time', models.TimeField()),
                ('medicine_contents', models.CharField(max_length=200)),
                ('pain', models.CharField(max_length=300)),
                ('pain_degree', models.IntegerField()),
                ('condition', models.TextField()),
                ('published_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
