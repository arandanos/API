# Generated by Django 4.1.1 on 2022-12-11 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename__feedback_feedback__name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.accessibleelement')),
            ],
        ),
    ]
