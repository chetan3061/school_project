# Generated by Django 3.0.2 on 2020-01-27 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='takes_web_lecture',
            field=models.BooleanField(default=False),
        ),
    ]