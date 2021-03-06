# Generated by Django 3.0.2 on 2020-01-27 08:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0002_auto_20200127_0800'),
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='classrooms.ClassRoom'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='per_class_duration',
            field=models.IntegerField(default=30, validators=[django.core.validators.MaxValueValidator(120), django.core.validators.MinValueValidator(30)]),
        ),
    ]
