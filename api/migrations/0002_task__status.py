# Generated by Django 4.1.1 on 2022-11-10 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='_status',
            field=models.BooleanField(default=False),
        ),
    ]
