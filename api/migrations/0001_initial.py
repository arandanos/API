# Generated by Django 4.1.1 on 2022-11-10 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessibleElement',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_text', models.TextField()),
                ('_pictogram', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_class_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.accessibleelement')),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.accessibleelement')),
            ],
        ),
        migrations.CreateModel(
            name='DishType',
            fields=[
                ('_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_feedback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.accessibleelement')),
            ],
        ),
        migrations.CreateModel(
            name='KitchenOrder',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_due_date', models.DateField()),
                ('_type', models.TextField()),
                ('_feedback', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.feedback')),
                ('_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.accessibleelement')),
            ],
        ),
        migrations.CreateModel(
            name='KitchenOrderDetail',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_quantity', models.IntegerField()),
                ('_classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.classroom')),
                ('_dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dish')),
                ('_kitchen_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.kitchenorder')),
            ],
        ),
        migrations.AddField(
            model_name='kitchenorder',
            name='_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.task'),
        ),
        migrations.AddField(
            model_name='dish',
            name='_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dishtype'),
        ),
    ]
