# Generated by Django 3.0 on 2023-01-13 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_created',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
