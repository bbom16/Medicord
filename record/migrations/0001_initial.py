# Generated by Django 2.1.4 on 2019-01-04 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_date', models.DateField(default=django.utils.timezone.now)),
                ('meal_time', models.TimeField()),
                ('meal_type', models.CharField(max_length=3)),
                ('meal_contents', models.TextField()),
                ('medicine_time', models.TimeField()),
                ('medicine_contents', models.CharField(max_length=200)),
                ('pain', models.CharField(max_length=300)),
                ('pain_degree', models.IntegerField()),
                ('condition', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]