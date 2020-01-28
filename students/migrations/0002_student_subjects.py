# Generated by Django 3.0.2 on 2020-01-27 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_auto_20200127_1110'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(blank=True, related_name='students', to='subjects.Subject'),
        ),
    ]
